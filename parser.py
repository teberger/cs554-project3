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
    graph = AGraph()
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

def to_string(root):
    if len(root.children) == 0:
        return str(root.value) + "\n";
    if root.value == ":=":
        return root.children[0].value + " := " + str(to_string(root.children[1])) + "\n"
    if root.value == "+" or root.value == "-" or root.value == "*" or root.value == "<" or root.value == ">" or root.value == ">=" or root.value == "<=" or root.value == "==" or root.value == "&&" or root.value == "||":
        return str(root.children[0].value) + " " + root.value + " " + str(root.children[1].value) + "\n"
    if root.value == "if":
        return "if " + str(to_string(root.children[0])) + "\n"
    if root.value == "not":
        return "not " + str(root.children[0].value) + "\n"
    if root.value == "while":
        return "if " + str(to_string(root.children[0])) + "\n"
def convert_to_cfg(root):
    id = 0
    graph = AGraph()
    program = ""
    revers_stack = []
    for x in root.children:
        revers_stack.append(x)
    stack = []
    while(len(revers_stack) != 0):
        stack.append(revers_stack.pop())
    layer_stack = []
    while(len(stack) != 0):
        print '--------------'
        print stack
        x = stack.pop()
        print x
        print layer_stack
        if x.value == 'if':
            temp = to_string(x)
            program += temp
            graph.add_node(id, label = program)
            if len(layer_stack) != 0:
                (temp,last_id) = layer_stack.pop()
                if temp == "endelse":
                    graph.add_edge(last_id, id)
                    (temp,last_id) = layer_stack.pop()
                    graph.add_edge(last_id, id)
                if temp == "if":
                    graph.add_edge(last_id, id)
                    layer_stack.append((temp,last_id))
            layer_stack.append(("if",id))
            program = ""
            id += 1
            stack.append(x.children[2])
            stack.append(x.children[1])
        elif x.value == "then" or x.value == "else":
            if x.value == "then":stack.append(node("endthen"))
            if x.value == "else":stack.append(node("endelse"))
            revers_stack = []
            for xx in x.children:
                revers_stack.append(xx)
            while(len(revers_stack) != 0):
                stack.append(revers_stack.pop())
        elif x.value == "endthen" or x.value == "endelse":
            print "program :"+program+str(id)
            print len(program)
            if len(program) != 0:
                graph.add_node(id, label = program)
            (temp, last_if_id) = layer_stack.pop()
            revers_stack = []
            while(temp != "if"):
                revers_stack.append((temp, last_if_id))
                (temp, last_if_id) = layer_stack.pop()
            while(len(revers_stack) != 0):
                layer_stack.append(revers_stack.pop())
            if len(program) != 0: graph.add_edge(last_if_id,id)
            if x.value == "endthen":
                layer_stack.append(("endthen",id))
                layer_stack.append((temp, last_if_id))

            if x.value == "endelse":
                (temp, last_then_id) = layer_stack.pop()
                #graph.add_edge(last_if_id, last_then_id)
                layer_stack.append(("endthen", last_then_id))
                layer_stack.append(("endelse", id))
            program = ""
            id += 1
        elif x.value == "while":
            temp = to_string(x)
            program += temp
        else:
            program += str(to_string(x))
    print layer_stack
    print graph
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


A = convert_to_graph(ast)

#print(A.string()) # print to screen
A.layout(prog='dot')
'''
print "writing to ast.dot"
A.write("ast.dot") # write to simple.dot
'''
print "printing to ast.png"
A.draw('ast.png',prog="dot") # draw to pngi using circo


cfg = convert_to_cfg(ast)
#print cfg.string()
cfg.layout(prog='dot')
print "printing to cfg.png"
cfg.draw('cfg.png',prog="dot") # draw to pngi using circo





























