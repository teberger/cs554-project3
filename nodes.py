#!/usr/bin/env python

""" Various custom AST node types that contain LLVM code generation methods. """

import antlr3
import antlr3.tree
from llvm.core import Module, Constant, Type, Value, ICMPEnum

from simpleLexer import *

# GLOBALS (directly from tutorials)
g_llvm_builder = None  # Builder created any time a function is entered.
tp_int = Type.int()
tp_bool = Type.int(1)


class EmitNode(antlr3.tree.CommonTree):
    def __init__(self, payload):
        super(EmitNode, self).__init__(payload)

        self.label = None
        """ The program point label of this node in the CFG. """

    def __str__(self):
        return self.text

    def emit(self):
        print "TYPE " + str(self.type) + " UNIMPLEMENTED"

    def getScope(self):
        """
        This will return the nearest BLOCK's scope. This is useful for updating
        a blocks scope from assignments.
        :rtype: dict[str, Value]
        """
        return self.parent.getScope()

    def getClosure(self):
        """
        Only Block nodes have variable scopes. Default behavior is to just ask
        for the parents closure. The root of the AST will always be a BLOCK, so
        it should always return from there.
        :rtype: dict[str, Value]
        """
        return self.parent.getClosure()


class BlockNode(EmitNode):
    def __init__(self, payload):
        super(BlockNode, self).__init__(payload)

        self.scope = {}
        """ The local scope for this block. """

        self.closure = None
        """ The closure of variables for this block. """

    def __str__(self):
        return '\n'.join([str(node) for node in self.children])

    def emit(self):
        for child in self.children:
            child.emit()
            # NOTE: Blocks do not have a return value!

    def initClosure(self):
        self.closure = []
        if self.parent is not None:
            # Use list() to create a new list rather than updating the parent's.
            self.closure = list(self.parent.getClosure())

        self.closure.append(self.scope)

    def getScope(self):
        """
        Returns this node's scope.
        :rtype: dict[str, llvm.core.PointerType]
        """
        return self.scope

    def getClosure(self):
        """
        Returns this node's closure. If the closure hasn't been initialized, do
        so first, then return it. This must be done here rather than in the
        constructor because parent/children data are not populated until AFTER
        the nodes have all been created.
        :rtype: dict[str, llvm.core.PointerType]
        """
        if self.closure is None:
            self.initClosure()
        return self.closure


class SkipNode(EmitNode):
    def __str__(self):
        return "Skip"

    def emit(self):
        # Emit useless instruction as a no-op.
        zero = Constant.int(tp_int, 0)
        return g_llvm_builder.add(zero, zero, "noop")


class IntegerNode(EmitNode):
    def __str__(self):
        return self.text

    def emit(self):
        return Constant.int(tp_int, self.text)


class IdentifierNode(EmitNode):
    def __str__(self):
        return self.text

    def emit(self):
        name = self.text
        scope = [scope for scope in self.getClosure() if name in scope]
        if scope:
            scope = scope[0]
            return g_llvm_builder.load(scope[name], name)
        else:
            raise RuntimeError("Unknown variable name: " + self.text)


class UnaryNode(EmitNode):
    def __str__(self):
        return str(self.children[0]) + str(self.children[1])

    def emit(self):
        op = self.children[0]
        expr = self.children[1].emit()
        if op.text == '-':
            return g_llvm_builder.neg(expr, "negated_" + expr.name)
        else:
            return expr


class BooleanNode(EmitNode):
    def __str__(self):
        return self.text

    def emit(self):
        if self.text.lower() == "true":
            return Constant.int(tp_bool, 1)
        elif self.text.lower() == "false":
            return Constant.int(tp_bool, 0)
        else:
            raise RuntimeError("Invalid boolean value.")


class UnaryBoolOpNode(EmitNode):
    def __str__(self):
        return str(self.children[0]) + str(self.children[1])

    def emit(self):
        b = self.children[0].emit()
        return g_llvm_builder.not_(b, "notbool")


class BinaryBoolOpNode(EmitNode):
    def __str__(self):
        left = self.children[0]
        right = self.children[1]
        return str(left) + " " + self.text + " " + str(right)

    def emit(self):
        left = self.children[0].emit()
        right = self.children[1].emit()

        if self.text.lower() == '&':
            return g_llvm_builder.and_(left, right, "and")
        elif self.text.lower() == '|':
            return g_llvm_builder.or_(left, right, "or")
        else:
            raise RuntimeError("Unrecognized binary boolean operator.")


class AssignmentNode(EmitNode):
    def __str__(self):
        left = self.children[0]
        right = self.children[1]
        return str(left) + " " + self.text + " " + str(right)

    def emit(self):
        name = self.children[0].text
        val = self.children[1].emit()

        # Find scope this variable exists in (if it exists already). If not,
        #  add the variable name to the current scope and allocate it.
        scope = [scope for scope in self.getClosure() if name in scope]
        if scope:
            scope = scope[0]  # Remove outer list generated by list comp.
        else:
            scope = self.getScope()
            scope[name] = g_llvm_builder.alloca(tp_int, name=name)

        # Update the value of the variable.
        return g_llvm_builder.store(val, scope[name])


class ArithmeticNode(EmitNode):
    def __str__(self):
        left = self.children[0]
        right = self.children[1]
        return str(left) + " " + self.text + " " + str(right)

    def emit(self):
        left = self.children[0].emit()
        right = self.children[1].emit()

        if self.text == '*':
            return g_llvm_builder.mul(left, right, 'mul')
        elif self.text == '+':
            return g_llvm_builder.add(left, right, 'add')
        elif self.text == '-':
            return g_llvm_builder.sub(left, right, 'sub')
        else:
            raise RuntimeError("Unrecognized arithmetic operator.")


class RelationalNode(EmitNode):
    def __str__(self):
        left = self.children[0]
        right = self.children[1]
        return str(left) + " " + self.text + " " + str(right)

    def emit(self):
        left = self.children[0].emit()
        right = self.children[1].emit()

        if self.text == '=':
            return g_llvm_builder.icmp(ICMPEnum.ICMP_EQ, left, right, "comp_eq")
        elif self.text == '<':
            return g_llvm_builder.icmp(ICMPEnum.ICMP_SLT, left, right, "comp_slt")
        elif self.text == '<=':
            return g_llvm_builder.icmp(ICMPEnum.ICMP_SLE, left, right, "comp_sle")
        elif self.text == '>':
            return g_llvm_builder.icmp(ICMPEnum.ICMP_SGT, left, right, "comp_sgt")
        elif self.text == '>=':
            return g_llvm_builder.icmp(ICMPEnum.ICMP_SGE, left, right, "comp_sge")
        else:
            raise RuntimeError("Unrecognized relational operator.")


class IfElseThenNode(EmitNode):
    def __str__(self):
        return "if " + str(self.children[0]) + " then"

    def emit(self):
        conditional = self.children[0].emit()
        then_branch = self.children[1]
        else_branch = self.children[2]

        # Create blocks for the if/then cases.
        function = g_llvm_builder.basic_block.function
        then_block = function.append_basic_block('then')
        else_block = function.append_basic_block('else')
        continue_block = function.append_basic_block('continue')

        # Emit conditional instruction.
        g_llvm_builder.cbranch(conditional, then_block, else_block)

        # Emit then block contents.
        g_llvm_builder.position_at_end(then_block)
        then_branch.emit()
        g_llvm_builder.branch(continue_block)

        # Emit else block contents.
        g_llvm_builder.position_at_end(else_block)
        else_branch.emit()
        g_llvm_builder.branch(continue_block)

        # Place the builder in the continue block so that the rest of the tree
        # can be generated.
        g_llvm_builder.position_at_end(continue_block)


class WhileNode(EmitNode):
    def __str__(self):
        return "while " + str(self.children[0])

    def emit(self):
        loop = self.children[1]

        # Create blocks for the if/then cases.
        function = g_llvm_builder.basic_block.function
        condition_block = function.append_basic_block('while_condition')
        loop_block = function.append_basic_block('while_loop')
        continue_block = function.append_basic_block('continue')

        # Emit unconditional jump into while loop conditional block.
        g_llvm_builder.branch(condition_block)

        # Check conditional, then either branch into loop or out of loop.
        g_llvm_builder.position_at_end(condition_block)
        conditional = self.children[0].emit()
        g_llvm_builder.cbranch(conditional, loop_block, continue_block)

        # Emit loop block contents.
        g_llvm_builder.position_at_end(loop_block)
        loop.emit()

        # Emit unconditional branch back to conditional block so another check
        # can be performed.
        g_llvm_builder.branch(condition_block)

        # Place the builder in the continue block so that the rest of the tree
        # can be generated.
        g_llvm_builder.position_at_end(continue_block)


class ErrorNode(antlr3.tree.CommonErrorNode):
    def emit(self):
        raise RuntimeError("Could not parse input:\n\n    " + self.getText())


class LlvmAdaptor(antlr3.tree.CommonTreeAdaptor):
    def createWithPayload(self, payload):
        if payload is None:
            return EmitNode(payload)

        # Fixes the problem where ANTLR3 produces Unicode objects instead of
        # Python string objects, and LLVM does not like Unicode objects.
        payload.text = str(payload.text)

        t = payload.type
        if t == BLOCK:
            return BlockNode(payload)
        if t == SKIP:
            return SkipNode(payload)
        elif t == INTEGER:
            return IntegerNode(payload)
        elif t == IDENT:
            return IdentifierNode(payload)
        elif t == UNARY:
            return UnaryNode(payload)
        elif t in (MULT, PLUS, MINUS):
            return ArithmeticNode(payload)
        elif t == RELOP:
            return RelationalNode(payload)
        elif t == BOOLEAN:
            return BooleanNode(payload)
        elif t == NOT:
            return UnaryBoolOpNode(payload)
        elif t in (AND, OR):
            return BinaryBoolOpNode(payload)
        elif t == GETS:
            return AssignmentNode(payload)
        elif t == IF:
            return IfElseThenNode(payload)
        elif t == WHILE:
            return WhileNode(payload)
        else:
            return EmitNode(payload)

    def errorNode(self, input, start, stop, exc):
        return ErrorNode(input, start, stop, exc)