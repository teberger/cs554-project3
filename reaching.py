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
    :rtype: dict[int, set[(str, str)]]
    """

    # Get generators for the various attributes for convenience.
    # TODO: Remove str() calls after debugging is finished!
    nodes = cfg.nodes()
    labels = (str(node.name) for node in nodes)
    variables = (str(node.attr["var"]) for node in nodes)
    types = (str(node.attr["type"]) for node in nodes)

    # Generate the genSet. For non assignment nodes, the value an empty set.
    genSets = dict()
    for node, label, variable, type in zip(nodes, labels, variables, types):
        genSets[label] = {(variable, label)} if type == NODE_ASSN else set()

    return genSets


def getKillSets(genSets):
    """
    Calculates a kill set for control-flow graph, given its gen set.

    The kill set is a dictionary with keys that map to the cfg's node labels.
    The values of this dictionary are sets of tuples. Each tuple in the set is
    of the form (variable name, label) where the variable name is a string and
    the label is an integer. Example:

        1 -> set((x, 9))
        2 -> set()
        3 -> set((y, 2), (z, 7))

    :param dict[int, set[(str, str)]] genSets: Gen set of the CFG.
    :rtype: dict[int, set[(str, int)]]
    """

    killSets = dict()

    # We'll be iterating over the gen set instead of the CFG because all of the
    # information we need to construct the kill set is contained in the gen set.
    # The kill set for a basic block is the set of all other generations for the
    # same variable, which is conveniently stored in the gen set.
    for label, genSet in genSets.iteritems():
        killSets[label] = set()

        # A basic block's gen set must have at least 1 item to have a kill set.
        # For each generation in a basic blocks gen set, retrieve the variable
        # that is generated so that we can look for generations in other basic
        # blocks' gen sets that modify the same variable.
        # Reminder: g = (var, label), so g[0] = var
        if genSet:
            for generation in genSet:
                variable = generation[0]

                # For each generation in each gen set (except generations with
                # the same label as the gen set we are inspecting, as those are
                # it's own generations!), for any generation that modifies the
                # same variable as the outer gen set, add that generation to the
                # kill set.
                for gs in genSets.values():
                    for v, l in gs:
                        if v == variable and l != label:
                            killSets[label] |= gs

    return killSets


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
    g.add_node("start", label="START",             type=NODE_NONE,     var='')
    g.add_node("0",    label="x := 4;",            type=NODE_ASSN,     var='x')
    g.add_node("1",    label="y := 7;",            type=NODE_ASSN,     var='y')
    g.add_node("2",    label="while x < 10 do",    type=NODE_WHILE,    var='')
    g.add_node("3",    label="if y > 3 then",      type=NODE_IF,       var='')
    g.add_node("4",    label="y := x + 1;",        type=NODE_ASSN,     var='y')
    g.add_node("5",    label="x := x + 1;",        type=NODE_ASSN,     var='x')
    g.add_node("6",    label="a := x + 1;",        type=NODE_ASSN,     var='a')
    g.add_node("7",    label="y := x + 2;",        type=NODE_ASSN,     var='y')
    g.add_node("8",    label="x := x + 1;",        type=NODE_ASSN,     var='x')
    g.add_node("end",   label="END",               type=NODE_NONE,     var='')

    # Edges
    g.add_edge("start", "0")
    g.add_edge("0", "1")
    g.add_edge("1", "2")
    g.add_edge("2", "3")
    g.add_edge("2", "end")
    g.add_edge("3", "4")
    g.add_edge("3", "6")
    g.add_edge("4", "5")
    g.add_edge("5", "8")
    g.add_edge("6", "7")
    g.add_edge("7", "8")
    g.add_edge("8", "2")

    # Output a diagram of the control-flow graph.
    g.draw("output/input2.png", format="png", prog="dot")

    genSets = getGenSets(g)
    killSets = getKillSets(genSets)

    print "GEN"
    print "==="

    for label, gs in sorted(genSets.iteritems()):
        print label, gs

    print
    print "KILL"
    print "===="
    for label, ks in sorted(killSets.iteritems()):
        print label, ks
