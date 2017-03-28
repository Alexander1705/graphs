#!/usr/bin/env python3

from typing import Set
from graphs import Graph, Node

filename = input('Входной файл: ')

with open(filename) as file:
    graph = Graph.read_adjacency_list(file, directed=True)

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

print('Найдено {} сильно связных компонент:'.format(len(components)))
for component in components:
    print(', '.join(str(node) for node in component))
