#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" A collection of functions for calculating reaching definitions.

    More here
"""
#TODO: Write more in header.
#TODO: NODE ASSUMPTIONS
# node.attr[type] -> some sort of type so we can differentiate assignments from ifs
NODE_NONE   =   unicode('0')   # start, end, skip
NODE_ASSN   =   unicode('1')
NODE_IF     =   unicode('2')
NODE_WHILE  =   unicode('3')
# node.attr[var] -> For assignment nodes, the name of the variable that is assigned.

from pygraphviz import AGraph


def getGenSets(cfg):
    """
    Calculates the gen sets for a labeled control-flow graph.

    The gen set is a dictionary with keys that map to the cfg's node labels. The
    values of this dictionary are sets of tuples. Each tuple in the set is of
    the form (variable name, label) where the variable name is a string and the
    label is an integer. Example:

        1 -> set((x, 1))
        2 -> set()
        3 -> set((y, 3), (z, 3))

    Due to the simple nature of our arithmetic grammar, these sets will always
    only contain one item because a single statement can not assign more than
    one variable. Also, the label number in the tuple will always be the key.

    :param AGraph cfg: The CFG for which to generate the gen set.
    :rtype: dict[int, set[(str, int)]]
    """
    # Get generators for the various attributes for convenience.
    nodes = cfg.nodes()
    labels = (node.name for node in nodes)
    variables = (node.attr["var"] for node in nodes)
    types = (node.attr["type"] for node in nodes)

    # Generate the genSet. For non assignment nodes, the value is None.
    genSet = dict()
    for node, label, variable, type in zip(nodes, labels, variables, types):
        genSet[label] = {(variable, label)} if type == NODE_ASSN else set()

    return genSet


def getKillSets(genSet):
    killSet = dict()
    for label, gen in genSet.iteritems():
        killSet[label] = set()
        if gen:
            # variable = gen.pop()[0]
            variable = next(iter(gen))[0]
            for gs in genSet.values():
                for v, l in gs:
                    if v == variable and l != label:
                        killSet[label] |= gs

    return killSet


if __name__ == "__main__":
    # Manually construct a CFG for testing purposes from the following code:
    #
    # x := 4;
    # y := 7;
    # while x < 10 do
    #     if y > 3 then
    #         y := x + 1;
    #         x := x + 1;
    #     else
    #         a := x + 1;
    #         y := x + 2;
    #     fi;
    #     x := x + 1;
    # od;
    #
    # This code was adapted from:
    # https://engineering.purdue.edu/~milind/ece573/2011spring/ps8-sol.pdf
    g = AGraph(directed=True)

    # Nodes
    g.add_node("start", label="START",              type=NODE_NONE,     var='')
    g.add_node("n0",    label="x := 4;",            type=NODE_ASSN,     var='x')
    g.add_node("n1",    label="y := 7;",            type=NODE_ASSN,     var='y')
    g.add_node("n2",    label="while x < 10 do",    type=NODE_WHILE,    var='')
    g.add_node("n3",    label="if y > 3 then",      type=NODE_IF,       var='')
    g.add_node("n4",    label="y := x + 1;",        type=NODE_ASSN,     var='y')
    g.add_node("n5",    label="x := x + 1;",        type=NODE_ASSN,     var='x')
    g.add_node("n6",    label="a := x + 1;",        type=NODE_ASSN,     var='a')
    g.add_node("n7",    label="y := x + 2;",        type=NODE_ASSN,     var='y')
    g.add_node("n8",    label="x := x + 1;",        type=NODE_ASSN,     var='x')
    g.add_node("end",   label="END",                type=NODE_NONE,     var='')

    # Edges
    g.add_edge("start", "n0")
    g.add_edge("n0", "n1")
    g.add_edge("n1", "n2")
    g.add_edge("n2", "n3")
    g.add_edge("n2", "end")
    g.add_edge("n3", "n4")
    g.add_edge("n3", "n6")
    g.add_edge("n4", "n5")
    g.add_edge("n5", "n8")
    g.add_edge("n6", "n7")
    g.add_edge("n7", "n8")
    g.add_edge("n8", "n2")

    # Output a diagram of the control-flow graph.
    g.draw("output/input2.png", format="png", prog="dot")

    genSets = getGenSets(g)
    killSets = getKillSets(genSets)

    print "GEN"
    for label, gs in genSets.iteritems():
        print label, gs

    print "KILL"
    for label, ks in killSets.iteritems():
        print label, ks
