#!/usr/bin/env python
import math

from graphs import Graph

filename = input('Input file: ')
directed = input('Is graph directed: ').lower() in {'y', 'yes'}

with open(filename) as file:
    graph = Graph.read_adjacency_list(file, directed)

source = graph[int(input('Source node: '))]
dest = graph[int(input('Destination: '))]

nodes = list(graph.nodes())

distances = {node: math.inf for node in nodes}
distances[source] = 0

while nodes:
    dmin = min(distances[node] for node in nodes)
    curr = next(filter(lambda node: distances[node] == dmin, nodes))

    for node in curr.successors():
        distances[node] = min(distances[node], dmin + graph[curr, node])

    nodes.remove(curr)

path = [dest]
curr = dest
while curr != source:
    curr = min(curr.predecessors(), key=lambda node: distances[node] + graph[(curr, node)])
    path.append(curr)
path = list(reversed(path))

print('One of shortest pathes is {}'.format(' -> '.join(str(node) for node in path)))

print('\n'.join('Distance between {} and {} is {}'.format(source, k, v) for k, v in distances.items()))
