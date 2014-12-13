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
    for x in revers_stack:
        stack.append(revers_stack.pop())
    layer_stack = []
    last_id = 0
    un_solved_stack = []
    while(len(stack) != 0):
        x = stack.pop()
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
            else_node = copy(x.children[2])
            then_node = copy(x.children[1])
            else_node.text = "else"
            then_node.text = "then"
            stack.push(else_node)
            stack.push(then_node)
            layer_stack.push("if", id)
            last_id = id
        elif x.text == "then":
            revers_stack = []
            for xx in x.children:
                revers_stack.append(xx)
            for xx in revers_stack:
                stack.append(revers_stack.pop())
        elif x.text == "else":
            un_solved_stack.push(last_id)
            revers_stack = []
            for xx in x.children:
                revers_stack.append(xx)
            for xx in revers_stack:
                stack.append(revers_stack.pop())
            (statement, id) = layer_stack.pop()
            last_id = id
        elif x.text == "fi":
            un_solved_stack.push(last_id)
        elif x.text == "while":
            program = "while " + render_short(x.children[0])
            graph.add_node(id, l = program)
            graph.add_edge(last_id,id)
            do_node = copy(x.children[1])
            do_node.text = "do"
            stack.push(do_node)
        elif x.text == "do":
            revers_stack = []
            for xx in x.children:
                revers_stack.append(xx)
            for xx in revers_stack:
                stack.append(xx)
        elif x.text == "od":
            un_solved_stack.push(last_id)
        id += 1
        program = ""
    return graph

print convert_ast_to_cfg()
