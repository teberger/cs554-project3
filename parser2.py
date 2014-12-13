from simple import SimpleParse
from pygraphviz import *
from copy import *

'''return the rhs of an assignment to string'''
def render_short(node):
    temp_program = ""
    x = node.text
    if x == "+" or x == "-" or x == "*" or x == ">" or x == "<" or x == ">=" or x == "<=" or x == "&&" or x == "||":
        temp_program = str(node.children[0].text) + " " + x + " " + str(node.children[1].text)
    elif x == "not":
        temp_program = x + " " + str(node.children[0].text)
    else:
        temp_program = str(x)
    return temp_program

'''converting an AST to CFG'''
def convert_ast_to_cfg(file):
    ast = SimpleParse(file)
    graph = AGraph()
    id = 0
    program = ""
    revers_stack = []
    for x in ast.children:
        revers_stack.append(x)
    stack = []
    while(len(revers_stack) != 0):
        stack.append(revers_stack.pop())
    layer_stack = []
    last_id = 0
    un_solved_stack = []
    while(len(stack) != 0):
        x = stack.pop()
	print x.text
        if x.text == ":=" or x.text == "skip":
            if x.text == "skip":
                program = "skip";
            else:
                program = str(x.children[0].text) + " := " + render_short(x.children[1])
            graph.add_node(id, l = program)
            graph.add_edge(last_id, id)
            last_id = id
        elif x.text == "if":
            program = "if " + render_short(x.children[0])
            graph.add_node(id, l = program)
            graph.add_edge(last_id, id)
            fi_node = copy(x.children[0])
	    else_node = copy(x.children[2])
            then_node = copy(x.children[1])
	    fi_node.token.text = "fi"
            else_node.token.text = "else"
            then_node.token.text = "then"
            stack.append(else_node)
            stack.append(then_node)
            layer_stack.append(("if", id))
            last_id = id
        elif x.text == "then":
            revers_stack = []
            for xx in x.children:
                revers_stack.append(xx)
            while(len(revers_stack) != 0):
                stack.append(revers_stack.pop())
        elif x.text == "else":
            un_solved_stack.append(last_id)
            revers_stack = []
            for xx in x.children:
                revers_stack.append(xx)
            while(len(revers_stack) != 0):
                stack.append(revers_stack.pop())
            (statement, last_id) = layer_stack.pop()
	    layer_stack.append((statement,last_id))
        elif x.text == "fi":
            un_solved_stack.append(last_id)
	    layer_stack.pop()
        elif x.text == "while":
            program = "while " + render_short(x.children[0])
            graph.add_node(id, l = program)
            graph.add_edge(last_id,id)
	    od_node = copy(x.children[0])
            do_node = copy(x.children[1])
	    od_node.token.text = "od"
            do_node.token.text = "do"
	    stack.append(od_node)
            stack.append(do_node)
	    layer_stack.append("while", id)
	    last_id = id
        elif x.text == "do":
            revers_stack = []
            for xx in x.children:
                revers_stack.append(xx)
            while(len(revers_stack) != 0):
                stack.append(xx)
        elif x.text == "od":
	    end_while_id = last_id
	    (statement, last_id) = layer_stack.pop()
            graph.add_edge(end_while_id, last_id)
	print "id:",id," statement: ",program
        id += 1
        program = ""
    return graph

print convert_ast_to_cfg("test.txt")
