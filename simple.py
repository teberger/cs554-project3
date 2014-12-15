#!/usr/bin/env python

""" Converts an abstract syntax tree (AST) produced by ANTLR3 into LLVM code,
    and produces an executable.
"""
import nodes
from nodes import *
import simple_graph

# ANTLR
import antlr3
import antlr3.tree
from simpleLexer import simpleLexer
from simpleParser import simpleParser

# LLVM
from llvm.core import Module, Type, Constant, Builder


def main(file):
    # Get the abstract syntax tree.
    try:
        ast = SimpleParse(file)
    except:
        print "Supplied file path is invalid!"
        return 1

    # Create main function.
    #
    # Create the main function signature and add it to the module.
    # Signature: int main()
    g_llvm_module = Module.new('simple')  # Holds all of the IR code.
    tp_main = Type.function(tp_int, [])
    f_main = g_llvm_module.add_function(tp_main, "main")

    # Set up the entry block for the main function and create a builder for it.
    entry_block = f_main.append_basic_block("entry")
    nodes.g_llvm_builder = Builder.new(entry_block)

    # Emit the programs main code.
    ast.emit()

    # Setup of printf and a formatting string for printing variables to stdout.
    f_printf = SetupPrintf(g_llvm_module)
    p_fs = EmitGlobalString(g_llvm_module, nodes.g_llvm_builder, "%s = %i\n")

    # Calls to printf to print out the variables.
    scope = ast.getScope()
    sorted_vars = sorted(list(scope))
    for var in sorted_vars:
        name = EmitGlobalString(g_llvm_module, nodes.g_llvm_builder, var)
        value = nodes.g_llvm_builder.load(scope[var])
        nodes.g_llvm_builder.call(f_printf, [p_fs, name, value])

    # Exit with return code 0 (RET_SUCCESS).
    nodes.g_llvm_builder.ret(Constant.int(tp_int, 0))

    ModuleToNativeBinary(g_llvm_module)
    nameMap = dict()
    LabelAst(ast, 0, nameMap)
    simple_graph.render_graph(ast)

    return 0

def SimpleParse(input):
    """
    Read an input file, lex, parse, and produce a tree.
    :param str input: Path to input file.
    :rtype: nodes.BlockNode
    """
    test_input = open(input).read()
    charStream = antlr3.StringStream(test_input)
    lexer = simpleLexer(charStream)
    tokenStream = antlr3.CommonTokenStream(lexer)
    parser = simpleParser(tokenStream)
    llvmAdaptor = LlvmAdaptor()
    parser.setTreeAdaptor(llvmAdaptor)
    return parser.program().tree


def LabelAst(ast, counter, nameMap):
    if type(ast) is AssignmentNode or type(ast) is SkipNode:
        ast.label = counter
        nameMap[ast.label] = ast
        return counter + 1
    elif type(ast) is IfElseThenNode:
        #condition is 0
        ast.label = counter
        nameMap[ast.label] = ast
        counter += 1
    elif type(ast) is WhileNode:
        ast.label = counter
        nameMap[ast.label] = ast
        counter += 1

    c = counter
    for child in ast.children:
        c = LabelAst(child, c, nameMap)

    return c


def AstToCfg(ast):
    pass


def EmitGlobalString(module, builder, g_string):
    """
    Emits a global string and returns a pointer to it.
    :param llvm.core.Module module: The current LLVM module.
    :param llvm.core.Builder builder: The current LLVM IR builder.
    :param str g_string: The string to emit.
    :rtype: llvm.core.PointerType
    """
    s = Constant.stringz(g_string)
    gs = module.add_global_variable(s.type, 'g_string')
    gs.initializer = s
    return builder.gep(gs,
                       [Constant.int(tp_int, 0), Constant.int(tp_int, 0)],
                       inbounds=True)


def SetupPrintf(module):
    """
    Emits the prototype for the libc printf function and returns the function.
    :param llvm.core.Module module: The current LLVM module.
    :param llvm.core.Builder builder: The current LLVM IR builder.
    :rtype: llvm.core.FunctionType
    """

    # Prototype printf from libc so that we can use it.
    tp_string = Type.pointer(Type.int(8))
    tp_print = Type.function(Type.void(), [tp_string], var_arg=True)
    return module.add_function(tp_print, 'printf')


def ModuleToNativeBinary(module):
    """
    Outputs an LLVM module to a native x86 Linux executable.
    :param llvm.Module module: The module to output.
    """
    obj = "simple_program.o"
    dst = "simple_program"

    with open(obj, 'wb') as f:
        module.to_native_object(f)

    import subprocess
    cmd = ['cc', '-o', dst, obj]
    r = subprocess.call(cmd)
    if r != 0:
        raise Exception("Failed to link with " + str(cmd))

if __name__ == "__main__":
    import sys

    # if len(sys.argv) != 2:
    #     print "Usage: simple.py file\n"

    sys.exit(main("input/input3.txt"))