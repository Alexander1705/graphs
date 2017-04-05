#!/usr/bin/env python3
import math

from graphs import Graph

filename = input('Input file [levit.graph]: ')
directed = input('Is graph directed [Y/n]: ').lower() in {'', 'y', 'yes'}

if not filename:
    filename = 'dantzig.graph'

with open(filename) as file:
    graph = Graph.read_adjacency_list(file, directed)

start = graph[int(input('Source node: '))]

A = graph.weight_matrix()

W = {}

for i, u in enumerate(graph.nodes()):
    W[u] = {}
    for j, v in enumerate(graph.nodes()):
        W[u][v] = A[i][j]

D = {node: math.inf for node in graph.nodes()}
P = {node: None for node in graph.nodes()}

D[start] = 0

M0 = []
M1 = [start]
M2 = [node for node in graph.nodes() if node != start]

while M1:
    print('D:', ', '.join(str(d) for d in D.values()))
    print('M0:', ', '.join(str(node) for node in M0))
    print('M1:', ', '.join(str(node) for node in M1))
    print('M2:', ', '.join(str(node) for node in M2))
    print()

    curr = M1.pop()
    M0.append(curr)
    for node in curr.successors():
        if node in M2:
            M2.remove(node)
            M1.append(node)
            D[node] = D[curr] + W[curr][node]
        elif node in M1:
            D[node] = min(D[node], D[curr] + W[curr][node])
        elif node in M0:
            if D[node] > D[curr] + W[curr][node]:
                D[node] = D[curr] + W[curr][node]
                M0.remove(node)
                M1.append(node)

for k, v in D.items():
    print(k, '-', v)