import graphviz
import pygraphviz

name_count = 0


def getName():
    """ Get a unique name for a node. """
    global name_count
    name_count += 1
    return 'n' + str(name_count)


def renderGraph(ast):
    """ Generate a digraph using Graphviz. """
    graph = graphviz.Digraph(format='png')
    treeWalk(graph, ast, None)
    graph.render('output/graph')


def treeWalk(graph, ast, parent):
    this_node = getName()
    # Only put a program point label if there is one!
    if ast.label is not None:
        graph.node(name=this_node, label="[" + str(ast.label) + "] " + ast.text)
    else:
        graph.node(name=this_node, label=ast.text)

    if parent is not None:
        graph.edge(parent, this_node)
    for child in ast.children:
        treeWalk(graph, child, this_node)


def renderCFG(transitions, nameMap):
    g = pygraphviz.AGraph(directed=True)
    for parent, child in transitions:
        if not g.has_node(parent):
            g.add_node(parent, label=str(nameMap[parent]))
        if not g.has_node(child):
            g.add_node(child, label=str(nameMap[child]))

        g.add_edge(parent, child)

    g.draw("output/cfg.png", format="png", prog="dot")
