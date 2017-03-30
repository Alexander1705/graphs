#!/usr/bin/env python3

from typing import Set
from graphs import Graph, Node

filename = input('Input file: ')

with open(filename) as file:
    graph = Graph.read(file, directed=True)

R = graph.reachability_matrix()

free_nodes = set(graph.nodes())
components = list()

while free_nodes:
    root = free_nodes.pop()
    component = {root}

    for node in free_nodes:
        if R[root][node] and R[node][root]:
            component.add(node)

    free_nodes = free_nodes.difference(component)
    components.append(component)

print("Strongly connected components:")
for i, component in enumerate(components, 1):
    print('{}: {}'.format(i, ', '.join(str(node) for node in component)))
