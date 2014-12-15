import graphviz

name_count = 0


def getName():
    """ Get a unique name for a node. """
    global name_count
    name_count += 1
    return 'n' + str(name_count)


def render_graph(ast):
    """ Generate a digraph using Graphviz. """
    graph = graphviz.Digraph(format='png')
    tree_walk(graph, ast, None)
    graph.render('output/graph')


def tree_walk(graph, ast, parent):
    this_node = getName()
    # Only put a program point label if there is one!
    if ast.label is not None:
        graph.node(name=this_node, label="[" + str(ast.label) + "] " + ast.text)
    else:
        graph.node(name=this_node, label=ast.text)

    if parent is not None:
        graph.edge(parent, this_node)
    for child in ast.children:
        tree_walk(graph, child, this_node)