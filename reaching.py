#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" A collection of functions for calculating reaching definitions. """

from pygraphviz import AGraph
from collections import deque


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
    :rtype: dict[str, set[(str, str)]]
    """

    # Get generators for the various attributes for convenience.
    nodes = cfg.nodes()
    labels = (node.name for node in nodes)
    variables = (node.attr["var"] for node in nodes)

    # Generate the genSet. For non assignment nodes, the value an empty set.
    genSets = dict()
    for node, label, variable in zip(nodes, labels, variables):
        genSets[label] = {(variable, label)} if variable != '' else set()

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

    :param dict[str, set[(str, str)]] genSets: Gen set of the CFG.
    :rtype: dict[str, set[(str, str)]]
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


def getInSet(label, cfg, outSets):
    """
    Calculates the IN set for a basic block (identified by its label).

    The IN set of a basic block is the union of OUT sets of its predecessors.
    The IN set is also the Reaching Definition (RD) Set.

    :param str label: The node for which to calculate the in set.
    :param AGraph cfg: The control-flow graph the node belongs to.
    :param dict[str, set[(str, str)]] outSets: Set of all out sets for the cfg.
    :rtype: set[(str, str)]
    """
    return set().union(*(outSets[p.name] for p in cfg.predecessors(label)))


def getOutSet(label, genSets, killSets, inSets):
    """
    Calculates the OUT set for a basic block (identified by its label).

    :param str label: The node ofr which to calculate the out set.
    :param dict[str, set[(str, str)]] genSets: Gen sets of the cfg.
    :param dict[str, set[(str, str)]] killSets: Kill sets of the cfg.
    :param dict[str, set[(str, str)]] inSets: IN sets of the cfg.
    :rtype: set[(str, str)]
    """
    return genSets[label] | (inSets[label] - killSets[label])


def getReachingDefinitions(cfg, startLabel):
    """
    Calculates the reaching definitions of a control-flow graph.

    :param AGraph cfg: The control-flow graph for which to calculate RDs.
    :param str startLabel: The label of the start node of the CFG.
    :rtype: dict[str, set[(str, str)]]
    """

    # Gen / Kill sets can be generated completely immediately.
    # IN / OUT start out empty initially.
    # The previousOut set is used to track changes to OUT sets during iteration.
    genSets = getGenSets(cfg)
    killSets = getKillSets(genSets)
    inSets = {label: set() for label in genSets}
    outSets = inSets.copy()
    previousOutSets = {label: None for label in genSets}

    # The iteration queue stores the next nodes to evaluate in the iteration.
    queue = deque([startLabel])

    while queue:
        label = queue.popleft()

        # Calculate (new) IN set.
        inSets[label] = getInSet(label, cfg, outSets)

        # Calculate the (new) OUT set, and check if it is different from the
        # previous version so we know whether or not to add the node's
        # successors to the iteration queue. The previous set is initially
        # populated by None, so every node will be visited at least once.
        outSet = getOutSet(label, genSets, killSets, inSets)
        if outSet != previousOutSets[label]:
            outSets[label] = outSet
            previousOutSets[label] = outSet
            queue.extend((s.name for s in cfg.successors(label) if s not in queue))

    return inSets


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
    g.add_node("start", label="START",              var='')
    g.add_node("0",     label="x := 4;",            var='x')
    g.add_node("1",     label="y := 7;",            var='y')
    g.add_node("2",     label="while x < 10 do",    var='')
    g.add_node("3",     label="if y > 3 then",      var='')
    g.add_node("4",     label="y := x + 1;",        var='y')
    g.add_node("5",     label="x := x + 1;",        var='x')
    g.add_node("6",     label="a := x + 1;",        var='a')
    g.add_node("7",     label="y := x + 2;",        var='y')
    g.add_node("8",     label="x := x + 1;",        var='x')
    g.add_node("end",   label="END",                var='')

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
    # g.draw("output/input2.png", format="png", prog="dot")

    rd = getReachingDefinitions(g, u"start")
    labels = sorted([k for k in rd.keys()])
    for label in labels:
        print label + ": ",
        for s in rd[label]:
            print "[" + s[0] + ", " + s[1] + "] ",
        print
