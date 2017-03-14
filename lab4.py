#!/usr/bin/env python

from graphs import Graph

filename = input('Input file: ')
directed = input('Is graph directed: ').lower() in {'y', 'yes'}
start = int(input('Start search from: '))

with open(filename) as file:
    g = Graph.read_adjacency_list(file, directed)

print('Depth-first search:')
g.depth_first_search(start)

print('Breadh-first search:')
g.breadth_first_search(start)