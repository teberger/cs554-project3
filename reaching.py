#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" A collection of functions for calculating reaching definitions.

    More here
"""
#TODO: Write more in header.

from pygraphviz import AGraph


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
    g.add_node("start", label="START")
    g.add_node("n0", label="x := 4;")
    g.add_node("n1", label="y := 7;")
    g.add_node("n2", label="while x < 10 do")
    g.add_node("n3", label="if y > 3 then")
    g.add_node("n4", label="y := x + 1;")
    g.add_node("n5", label="x := x + 1;")
    g.add_node("n6", label="a := x + 1;")
    g.add_node("n7", label="y := x + 2;")
    g.add_node("n8", label="x := x + 1;")
    g.add_node("end", label="END")

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
