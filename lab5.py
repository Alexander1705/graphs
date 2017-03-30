#!/usr/bin/env python

from graphs import Graph

filename = input('Input file: ')

with open(filename) as file:
    graph = Graph.read(file, directed=True)

nodes = list(graph.nodes())
sorted_nodes = []
while nodes:
    for node in nodes:
        if all(p in sorted_nodes for p in node.predecessors()):
            sorted_nodes.append(node)
            nodes.remove(node)
            break
    else:
        print('Impossible to do topological sorting')
        break
else:
    print(sorted_nodes)
