#!/usr/bin/env python3
from graphs import Graph

filename = input('Input file [dantzig.graph]: ')
directed = input('Is graph directed [Y/n]: ').lower() in {'', 'y', 'yes'}

if not filename:
    filename = 'dantzig.graph'

with open(filename) as file:
    graph = Graph.read_adjacency_list(file, directed)

A = graph.weight_matrix()
D = graph.weight_matrix()
n = len(D)

for i in range(n):
    A[i][i] = D[i][i] = 0

for m in range(1, n+1):
    for i in range(m-1):
        D[i][m-1] = min(A[j][m-1] + D[i][j] for j in range(m-1))

    for j in range(m-1):
        D[m-1][j] = min(A[m-1][i] + D[i][j] for i in range(m-1))

    for i in range(m-1):
        for j in range(m-1):
            D[i][j] = min(D[i][m-1] + D[m-1][j], D[i][j])

    for i in range(m):
        print(''.join('{:^5}'.format(D[i][j]) for j in range(m)))
    print()

nodes = list(graph.nodes())
print('Distance matrix:')
for i, row in enumerate(D):
    print(nodes[i], ''.join('{:^5}'.format(i) for i in row))
