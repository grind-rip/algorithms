"""
Depth-first Search (DFS)
------------------------
"""

from unittest import TestCase

from src import depth_first_search
from src.shared.node import Node


class TestDepthFirstSearch(TestCase):
    # Create the following tree:
    #
    #          A
    #          ●
    #        /   \
    #      B       C
    #      ●       ●
    #    /   \   /   \
    #   D     E F     G
    #   ●     ● ●     ●

    def setUp(self):
        # Create nodes
        self.A = Node(value="A")
        self.B = Node(value="B")
        self.C = Node(value="C")
        self.D = Node(value="D")
        self.E = Node(value="E")
        self.F = Node(value="F")
        self.G = Node(value="G")

        # Set up parent relationships
        self.B.parent, self.C.parent = self.A, self.A
        self.D.parent, self.E.parent = self.B, self.B
        self.F.parent, self.G.parent = self.C, self.C

        # Set up child relationships
        self.A.children = [self.B, self.C]
        self.B.children = [self.D, self.E]
        self.C.children = [self.F, self.G]

        # Set root node
        self.root = self.A

    def test_depth_first_search_recursive(self):
        exp = ["A", "B", "D", "E", "C", "F", "G"]
        assert depth_first_search.depth_first_search_recursive(self.root) == exp

    def test_depth_first_search_iterative(self):
        exp = ["A", "C", "G", "F", "B", "E", "D"]
        assert depth_first_search.depth_first_search_iterative(self.root) == exp
