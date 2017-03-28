import sys


class Node(object):
    def __init__(self, label, graph=None):
        self.label = label
        self._graph = graph

    def neighbors(self):
        for node in self._graph.nodes():
            if (self, node) in self._graph or (node, self) in self._graph:
                yield node

    def successors(self):
        for node in self._graph.nodes():
            if (self, node) in self._graph:
                yield node

    def predecessors(self):
        for node in self._graph.nodes():
            if (node, self) in self._graph:
                yield node

    def __hash__(self):
        return hash(self.label)

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.label == other.label
        else:
            return self.label == other

    def __str__(self):
        return str(self.label)

    def __repr__(self):
        return str(self.label)


class Graph(object):
    def __init__(self, directed=False):
        self._directed = directed
        self._graph = {}

    def is_directed(self):
        return self._directed

    def add_node(self, node):
        if node not in self._graph:
            self._graph[node] = set()

    def add_edge(self, u, v):
        self.add_node(u)
        self.add_node(v)

        self._graph[u].add(v)

        if not self.is_directed():
            self._graph[v].add(u)

    def nodes(self):
        return (Node(label, self) for label in self._graph.keys())

    def edges(self):
        for u in self._graph.keys():
            for v in self._graph[u]:
                yield (u, v)

    def adjacency_matrix(self):
        return {
            u: {v: True if v in self._graph[u] else False for v in self._graph.keys()}
            for u in self._graph.keys()
        }

    def reachability_matrix(self):
        R = self.adjacency_matrix()

        for node in self.nodes():
            R[node][node] = True

        for k in self.nodes():
            for i in self.nodes():
                for j in self.nodes():
                    R[i][j] = R[i][j] or R[i][k] and R[k][j]

        return R

    def __contains__(self, item):
        if isinstance(item, tuple):
            # Item is an edge
            u, v = item
            if isinstance(u, Node):
                u = u.label
            if isinstance(v, Node):
                v = v.label

            return (u, v) in self._edges or not self.is_directed() and (v, u) in self._edges
        else:
            # Item is a node
            if isinstance(item, Node):
                item = item.label

            return item.label in self._nodes

    def depth_first_search(self, start):
        if not isinstance(start, Node):
            start = Node(start, self)

        stack = [start]
        visited = set()

        while stack:
            node = stack[-1]

            if node not in visited:
                print('{}: node {}, stack - {}'.format(len(visited)+1, node, stack))

            visited.add(node)

            for succ in node.successors():
                if succ not in visited:
                    stack.append(succ)
                    break

            if node == stack[-1]:
                node = stack.pop()
                print('-: node {}, stack - {}'.format(node, stack))

    def breadth_first_search(self, start):
        if not isinstance(start, Node):
            start = Node(start, self)

        queue = [start]
        visited = {start}

        i = 1
        while queue:
            node = queue[0]
            print('{}: node {}, queue - {}'.format(i, start, queue))
            for succ in node.successors():
                if succ not in visited:
                    queue.append(succ)
                    visited.add(succ)
                    print('-: node {}, queue - {}'.format(node, queue))
            del queue[0]
            print('-: node {}, queue - {}'.format(node, queue))
            i += 1

    @staticmethod
    def read_adjacency_list(file=sys.stdin, directed=False):
        graph = Graph(directed)

        n, m = map(int, file.readline().split())

        for i in range(1, n+1):
            graph.add_node(i)

        for line in file.readlines():
            u, v = map(int, line.split())

            graph.add_edge(u, v)

        return graph
