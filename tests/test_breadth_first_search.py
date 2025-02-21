"""
Breadth-first Search (BFS)
--------------------------
"""

from unittest import TestCase

from src import breadth_first_search
from src.shared.node import Node


class TestBreadthFirstSearch(TestCase):
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

    def test_breadth_first_search(self):
        exp = ["A", "B", "C", "D", "E", "F", "G"]
        assert breadth_first_search.breadth_first_search(self.root) == exp

    def test_shortest_path(self):
        exp = ["A", "C", "G"]
        assert breadth_first_search.shortest_path(self.root, self.G) == exp

    def test_shortest_path_parent_pointers(self):
        exp = ["A", "C", "G"]
        assert (
            breadth_first_search.shortest_path_parent_pointers(self.root, self.G) == exp
        )
