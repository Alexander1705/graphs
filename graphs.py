import sys, math

from typing import Union, List


class Node(object):
    def __init__(self, label, graph=None):
        self.label = label
        self.graph = graph
        self.color = None

    def neighbours(self):
        return self.graph.backend.neighbours(self)

    def successors(self):
        return self.graph.backend.successors(self)

    def predecessors(self):
        return self.graph.backend.predecessors(self)

    def __str__(self):
        return str(self.label)

    def __repr__(self):
        return 'Node({}, {})'.format(self.label, self.graph)

    def __hash__(self):
        return hash(self.label)

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.label == other.label
        else:
            return self.label == other


class Edge(object):
    def __init__(self, u, v, weight=1):
        self.u = u
        self.v = v
        self.weight = weight


class WeightMatrix(object):
    def __init__(self, graph, directed):
        self.graph = graph
        self.directed = directed
        self._nodes = list()
        self.matrix: List[List[Union[int, float]]] = list()

    def nodes(self):
        return iter(self._nodes)

    def edges(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                yield (self._nodes[i], self._nodes[j], self.matrix[i][j])

    def add_node(self, label):
        if label in self._nodes:
            return

        self._nodes.append(Node(label, self.graph))

        for row in self.matrix:
            row.append(math.inf)

        self.matrix.append([math.inf for _ in range(len(self._nodes))])
        self.matrix[-1][-1] = 0

    def add_edge(self, u, v, weight=1):
        self.add_node(u)
        self.add_node(v)

        i = self._nodes.index(u)
        j = self._nodes.index(v)

        self.matrix[i][j] = weight

        if not self.directed:
            self.matrix[j][i] = weight

    def successors(self, node):
        i = self._nodes.index(node)

        for j in range(len(self.matrix)):
            if self.matrix[i][j] < math.inf:
                yield self._nodes[j]

    def predecessors(self, node):
        j = self._nodes.index(node)

        for i in range(len(self.matrix)):
            if self.matrix[i][j] < math.inf:
                yield self._nodes[i]

    def weight_matrix(self):
        return self.matrix

    def __getitem__(self, item):
        if isinstance(item, tuple):
            return self.matrix[self._nodes.index(item[0])][self._nodes.index(item[1])]
        return self._nodes[self._nodes.index(item)]


class Graph(object):
    def __init__(self, directed=True, backend=WeightMatrix):
        self.directed = directed
        self.backend: WeightMatrix = backend(self, directed)

    def nodes(self):
        return self.backend.nodes()

    def add_node(self, label):
        self.backend.add_node(label)

    def add_edge(self, u, v, weight=1):
        self.backend.add_edge(u, v, weight)

    def adjacency_matrix(self):
        return [
            [
                1 if v in u.successors() else 0
                for v in self.nodes()
            ] for u in self.nodes()
        ]

    def weight_matrix(self):
        return self.backend.weight_matrix()

    def __getitem__(self, item):
        return self.backend[item]

    @staticmethod
    def read_adjacency_list(file=sys.stdin, directed=True, backend=WeightMatrix):
        graph = Graph(directed, backend)

        n, m = map(int, file.readline().split())

        for line in file:
            graph.add_edge(*map(int, line.split()))

        return graph
