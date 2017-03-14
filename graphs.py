class Node(object):
    def __init__(self, label, graph=None):
        self.label = label
        self._graph = graph

    def neighbors(self):
        pass

    def successors(self):
        pass

    def predecessors(self):
        pass


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
