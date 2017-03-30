#!/usr/bin/env python

from graphs import Graph

filename = input('Input file: ')
directed = input('Is graph directed: ').lower() in {'y', 'yes'}
start = int(input('Start search from: '))

with open(filename) as file:
    g = Graph.read(file, directed)

print('\nDepth-first search:')
g.depth_first_search(start)

print('\nBreadh-first search:')
g.breadth_first_search(start)