#!/usr/bin/env python
from graphs import Graph

filename = input('Input file: ')
directed = input('Is graph directed: ').lower() in {'y', 'yes'}

with open(filename) as file:
    graph = Graph.read_adjacency_list(file, directed)

source = graph[int(input('Source node: '))]
dest = graph[int(input('Destination: '))]

parents = {node: None for node in graph.nodes()}
visited = {node: False for node in graph.nodes()}
passed = {u: {v: False for v in graph.nodes()} for u in graph.nodes()}

path = []

curr = source
while curr != dest:
    visited[curr] = True
    path.append(curr)
    try:
        node = next(filter(lambda node: not visited[node] and not passed[curr][node] and node != parents[curr], curr.successors()))
        passed[curr][node] = True
        parents[node] = curr
        curr = node
    except StopIteration:
        passed[curr][parents[curr]] = True
        curr = parents[curr]
path.append(dest)

print(' -> '.join(str(node) for node in path))
