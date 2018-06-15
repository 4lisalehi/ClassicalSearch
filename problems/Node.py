from algorithms.consts import INF


class Node:

    def __init__(self, state, g=0, h=0, parent_node=None):
        self.state = state
        self.g = g
        self.h = h
        self.gh = self.g + self.h
        self.parent_node = parent_node

    def __lt__(self, other):
        return self.gh < other.gh
