#!/usr/bin/env python3
import math
from collections import deque

filename = input('Maze file: ')
x0, y0 = map(int, input('Start: ').split())
x1, y1 = map(int, input('Destination: ').split())

maze = []

with open(filename) as file:

    for line in file:
        maze.append(list('#' + line.strip() + '#'))
        for i in range(len(maze[-1])):
            if maze[-1][i] == '.':
                maze[-1][i] = math.inf

    maze.insert(0, list('#' * len(maze[0])))
    maze.append(maze[0])

maze[x0][y0] = 0

queue = deque([(x0, y0)])

while queue:
    curr_x, curr_y = queue.popleft()

    for x, y in {(curr_x-1, curr_y), (curr_x+1, curr_y), (curr_x, curr_y-1), (curr_x, curr_y+1)}:
        if maze[x][y] != '#':
            if maze[x][y] > maze[curr_x][curr_y] + 1:
                maze[x][y] = maze[curr_x][curr_y] + 1
                queue.append((x, y))

maze_g = [['#' if maze[i][j] == '#' else ' ' for j in range(len(maze[0]))] for i in range(len(maze))]
maze_g[x0][y0] = '*'
curr_x, curr_y = x1, y1
while x != x0 or y != y0:
    for x, y in {(curr_x - 1, curr_y), (curr_x + 1, curr_y), (curr_x, curr_y - 1), (curr_x, curr_y + 1)}:
        if maze[x][y] != '#' and maze[x][y] < maze[curr_x][curr_y]:
            maze_g[curr_x][curr_y] = '*'
            curr_x, curr_y = x, y

for row in maze_g:
    print(''.join(row))
