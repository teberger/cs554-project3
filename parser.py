from pyparsing import *
from types import *
from copy import *
from pygraphviz import *


class node(object):
    def __init__(self, value, children = []):
        self.value = value
        self.children = children
    
    def __repr__(self, level=0):
        ret = "\t"*level+repr(self.value)+"\n"
        for child in self.children:
            ret += child.__repr__(level+1)
        return ret
    
    def delete_child(self, child):
        self.children.remove(child)
    
    def add(self,value):
        self.children.append(node(value))

def render(root):
    if root.value == '$' or root.value == 'then' or root.value == 'else' or root.value == 'do':
        process = root.children
        root.children = []
    else:
        process = root.value
        root.value = ''
        root.children = []
    if(type(process) is IntType or type(process) is StringType):
        root.value = process
    elif(len(process) == 1):
        root.value = process[0]
    else:
        list = []
        sub_list = []
        st = []
        for x in process:
            if x == 'if' or x == 'then' or x == 'else' or x == 'while' or x == 'do':
                sub_list.append(x)
                st.append(x)
            elif x == ";":
                if len(st) == 0 and len(sub_list) != 0:
                    temp = copy(sub_list)
                    list.append(temp)
                    sub_list = []
                    temp = []
                elif len(sub_list) != 0:
                    sub_list.append(x)
            elif x == 'fi' or x == 'od':
                if x == 'fi':
                    sub_list.append(x)
                    st.pop()
                    st.pop()
                    st.pop()
                else:
                    sub_list.append(x)
                    st.pop()
                    st.pop()
                if len(st) == 0:
                    temp = copy(sub_list)
                    list.append(temp)
                    sub_list = []
                    temp = []
            else:
                sub_list.append(x)
        if len(sub_list) != 0:
            temp = copy(sub_list)
            list.append(temp)

        if(len(list) > 1 or root.value == '$' or root.value == 'then' or root.value == 'else' or root.value == 'do'):
            for x in list:
                root.children.append(node(x))
        elif(list[0][0] == 'if'):
            root.value = 'if'
            list[0].remove('if')
            list2 = []
            sub_list = []
            st = []
            temp = []
            for x in list[0]:
                if (x == 'then' or x == 'else' or x == 'fi') and len(st) == 0:
                    temp = copy(sub_list)
                    list2.append(temp)
                    temp = []
                    sub_list = []
                elif x == 'fi':
                    sub_list.append(x)
                    st.pop()
                    st.pop()
                    st.pop()
                elif x == 'then' or x == 'else' or x == 'if':
                    sub_list.append(x)
                    st.append(x)
                else:
                    sub_list.append(x)
            root.children.append(node(list2[0]))
            root.children.append(node('then', list2[1]))
            root.children.append(node('else', list2[2]))
        elif(list[0][0] == 'while'):
            root.value = 'while'
            list[0].remove('while')
            list2 = []
            sub_list = []
            st = []
            temp = []
            for x in list[0]:
                if(x == 'do' or x == 'od') and len(st) == 0:
                    temp = copy(sub_list)
                    list2.append(temp)
                    temp = []
                    sub_list = []
                elif x == 'od':
                    sub_list.append(x)
                    st.pop()
                    st.pop()
                elif x == 'while' or x == 'do':
                    sub_list.append(x)
                    st.append(x)
                else:
                    sub_list.append(x)
            root.children.append(node(list2[0]))
            root.children.append(node('do', list2[1]))
        elif(list[0][0] == 'skip'):
            root.value = 'skip'
        elif(len(list[0]) > 1):
            if(list[0][0] == 'not'):
                root.value = 'not'
                root.children.append(node(list[0][1:]))
            else:
                root.value = list[0][1]
                root.children.append(node(list[0][0]))
                root.children.append(node(list[0][2:]))

    for x in root.children:
        render(x)

def convert_to_graph(root):
    id = 1
    queue = []
    graph = AGraph();
    graph.add_node(0, label = root.value)
    queue.append((0,root))
    while(len(queue) != 0):
        (new_id,new_root) = queue.pop(0)
        if(len(new_root.children) != 0):
            for x in new_root.children:
                graph.add_node(id, label = x.value)
                graph.add_edge(new_id, id)
                queue.append((id, x))
                id += 1
    return graph


boolean_op = oneOf('&& ||')
arith_bool_op = oneOf('== >= <= > <')
arith_op = oneOf('+ - *')
integer_value = Word(nums).setParseAction(lambda t:int(t[0]))
boolean_value = Keyword("true") | Keyword("false")
variable = Word( srange("[a-zA-Z_]"), srange("[a-zA-Z0-9_]") )
integer_variable = variable | integer_value
boolean_variable = variable | boolean_value


boolean_operation = integer_variable + arith_bool_op + integer_variable | boolean_variable + boolean_op + boolean_variable | Keyword("not") + boolean_variable | boolean_variable

operation = Keyword("not") + boolean_variable | integer_variable + arith_bool_op + integer_variable | integer_variable + arith_op + integer_variable | boolean_variable + boolean_op + boolean_variable | integer_value | boolean_value | variable

simple_stmt = Keyword("skip") | variable + ":=" + operation

stmt = Forward()
stmt << ((simple_stmt + ";" + stmt) | "while" + boolean_operation + "do" + stmt + "od" + Optional(";" + stmt) | "if" + boolean_operation + "then" + stmt + "else" + stmt + "fi" + Optional(";" + stmt) | simple_stmt)


parsed_list = stmt.parseFile("test.txt")
ast = node('$',parsed_list)
render(ast)
print ast

'''
A = convert_to_graph(ast)

print(A.string()) # print to screen
A.layout(prog='dot')
print "writing to ast.dot"
A.write("ast.dot") # write to simple.dot
print "printing to ast.png"
A.draw('ast.png',prog="dot") # draw to pngi using circo
'''

from llvm import *
from llvm.core import *
from llvm.ee import *
my_module = Module.new('cs554_llvm')
my_named_location = {}
my_named_values = {}

ty_int = Type.int()
ty_func = Type.function(Type.int(),[])

f_main = my_module.add_function(ty_func,"main")
entry = f_main.append_basic_block("entry")

my_builder = Builder.new(entry)

def CodeGen(root):
#	print '-------', root.value
	if root.value == '$':
		for x in root.children:
			CodeGen(x)
	elif root.value == ':=':
		right = CodeGen(root.children[1])
		if root.children[0].value not in my_named_values:
			my_named_location[root.children[0].value] = my_builder.alloca(Type.int(), name = root.children[0].value)
			my_builder.store(right, my_named_location[root.children[0].value])
		else:
			a = my_named_location[root.children[0].value]
			my_builder.store(right, a)
		my_named_values[root.children[0].value] = right
	elif root.value == '+' or root.value == '-' or root.value == '*':
		left = CodeGen(root.children[0])
		right = CodeGen(root.children[1])
		if root.value == '+':
			return my_builder.add(left, right, name = 'plustemp')
		elif root.value == '-':
			return my_builder.sub(left, right, name = 'subtemp')
		else:
			return my_builder.mul(left, right, name = 'multemp')
	elif root.value == '&&' or root.value == '||':
		left = CodeGen(root.children[0])
		right = CodeGen(root.children[1])
		a = my_builder.alloca(Type.int(1), name = 'temp')
		if root.value == '&&':
			value = my_builder.and_(left,right, name = 'temp')
		else:
			value = my_builder.or_(left,right, name = 'temp')
		my_builder.store(value, a)
		return value
	elif root.value == '>' or root.value == '<' or root.value == '==' or root.value == '<=' or root.value == '>=':
		left = CodeGen(root.children[0])
		right = CodeGen(root.children[1])
		a = my_builder.alloca(Type.int(1), name = 'temp')
		if root.value == '>':
			value = my_builder.icmp(ICMP_UGT,left, right, name = 'temp')
		elif root.value == '<':
			value = my_builder.icmp(ICMP_ULT, left, right, name = 'temp')
		elif root.value == '==':
			value =  my_builder.icmp(ICMP_EQ, left, right, name = 'temp')
		elif root.value == '<=':
			value =  my_builder.icmp(ICMP_UGE, left, right, name = 'temp')
		else:
			my_builder.icmp(ICMP_ULE, left, right, name = 'temp')
		my_builder.store(value, a)
		return value
	elif root.value == 'not':
		val = CodeGen(root.children[0])
		a = my_builder.alloca(Type.int(1), name = 'temp')
		value = my_builder.not_(val,'temp')
		my_builder.store(value, a)
		return value
	elif root.value == 'true' or root.value == 'false':
		if root.value == 'true':
			return  Constant.int(Type.int(1), 1)
		else:
			return  Constant.int(Type.int(1), 0)
	elif root.value == 'if':
		condition_bool = CodeGen(root.children[0])
		a = my_builder.alloca(Type.int(1), name = 'while_condition')
		my_builder.store(condition_bool, a)

		then_block = f_main.append_basic_block('then')
		else_block = f_main.append_basic_block('else')
		merge_block = f_main.append_basic_block('ifcond')
		
		my_builder.cbranch(condition_bool, then_block, else_block)

		my_builder.position_at_end(then_block)
		CodeGen(root.children[1])
		my_builder.branch(merge_block)

		then_block = my_builder.basic_block

		my_builder.position_at_end(else_block)
		CodeGen(root.children[2])
		my_builder.branch(merge_block)

		else_block = my_builder.basic_block

		my_builder.position_at_end(merge_block)
	elif root.value == 'while':
		condition_bool = CodeGen(root.children[0])
		a = my_builder.alloca(Type.int(1), name = 'while_condition')
		my_builder.store(condition_bool, a)


		do_block = f_main.append_basic_block('do')
		merge_block = f_main.append_basic_block('whilecond')
		
		my_builder.cbranch(condition_bool, do_block, merge_block)

		my_builder.position_at_end(do_block)
		CodeGen(root.children[1])

		condition_bool = CodeGen(root.children[0])
		my_builder.store(condition_bool, a)
		
		my_builder.cbranch(condition_bool, do_block, merge_block)
		
		do_block = my_builder.basic_block

		my_builder.position_at_end(merge_block)
	elif root.value == 'then' or root.value == 'else' or root.value == 'do':
		for x in root.children:
			if x == 'skip':
				return
			else:
				CodeGen(x)
	elif root.value == 'skip':
		return
	elif root.value in my_named_values:
		return my_named_values[root.value]
	else:
		return  Constant.int(Type.int(), root.value)

CodeGen(ast)
print my_module

result = my_builder.call(f_main, [])
print(result)
'''
s = Constant.stringz("The Answer(tm): %d\n")
gs = my_module.add_global_variable(s.type, 'result_fmt')
gs.initializer = s
p_gs = my_builder.gep(gs,[Constant.int(Type.int(), 0), Constant.int(Type.int(), 0)],inbounds=True)

tp_string = Type.pointer(Type.int(8))

tp_print = Type.function(Type.void(), [tp_string], var_arg=True)

f_printf = my_module.add_function(tp_print, 'printf')

my_builder.call(f_printf, [p_gs, result])
my_builder.ret(Constant.int(Type.int(), 0))

print("* LLVM IR")

print(my_module)

print("* Verification")

my_module.verify()

obj = 'llvm_ast.o'

dst = 'llvm_ast'
with open(obj, 'wb') as f:
        my_module.to_native_object(f)

import subprocess

cmd = ['cc', '-o', dst, obj]

r = subprocess.call(cmd)

if r != 0:
	raise Exception("Failed to link with " + str(cmd))
	'''
