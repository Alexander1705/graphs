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


class Graph(object):
    def __init__(self, directed=False):
        self._directed = directed
        self._nodes = set()
        self._edges = set()

    def is_directed(self):
        return self._directed

    def add_node(self, node):
        self._nodes.add(node)

    def add_edge(self, u, v):
        self._edges.add((u, v))

        if not self.is_directed():
            self._edges.add((v, u))

    def nodes(self):
        return (Node(label, self) for label in self._nodes)

    def edges(self):
        return ((Node(u, self), Node(v, self)) for u, v in self._edges)

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
