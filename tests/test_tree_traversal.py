"""
Tree Traversal
--------------
"""

from unittest import TestCase

from src import tree_traversal
from src.shared.tree_node import TreeNode


class TestTreeTraversal(TestCase):
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
        self.A = TreeNode(value="A")
        self.B = TreeNode(value="B")
        self.C = TreeNode(value="C")
        self.D = TreeNode(value="D")
        self.E = TreeNode(value="E")
        self.F = TreeNode(value="F")
        self.G = TreeNode(value="G")

        # Set up parent relationships
        self.B.parent, self.C.parent = self.A, self.A
        self.D.parent, self.E.parent = self.B, self.B
        self.F.parent, self.G.parent = self.C, self.C

        # Set up child relationships
        self.A.left, self.A.right = self.B, self.C
        self.B.left, self.B.right = self.D, self.E
        self.C.left, self.C.right = self.F, self.G

        # Set root node
        self.root = self.A

    def test_depth_first_search_recursive_pre_order(self):
        exp = ["A", "B", "D", "E", "C", "F", "G"]
        assert tree_traversal.depth_first_search_recursive_pre_order(self.root) == exp

    def test_depth_first_search_iterative_pre_order(self):
        exp = ["A", "B", "D", "E", "C", "F", "G"]
        assert tree_traversal.depth_first_search_iterative_pre_order(self.root) == exp

    def test_depth_first_search_recursive_post_order(self):
        exp = ["D", "E", "B", "F", "G", "C", "A"]
        assert tree_traversal.depth_first_search_recursive_post_order(self.root) == exp

    def test_depth_first_search_iterative_post_order(self):
        exp = ["D", "E", "B", "F", "G", "C", "A"]
        assert tree_traversal.depth_first_search_iterative_post_order(self.root) == exp

    def test_depth_first_search_recursive_in_order(self):
        exp = ["D", "B", "E", "A", "F", "C", "G"]
        assert tree_traversal.depth_first_search_recursive_in_order(self.root) == exp

    def test_depth_first_search_iterative_in_order(self):
        exp = ["D", "B", "E", "A", "F", "C", "G"]
        assert tree_traversal.depth_first_search_iterative_in_order(self.root) == exp

    def test_breadth_first_search(self):
        exp = ["A", "B", "C", "D", "E", "F", "G"]
        assert tree_traversal.breadth_first_search(self.root) == exp
