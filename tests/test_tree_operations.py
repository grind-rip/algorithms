"""
Tree Operations
---------------
"""

from unittest import TestCase

from src import tree_operations
from src.shared.tree_node import TreeNode
from tests.utils import assert_tree


class TestTreeOperations(TestCase):
    # Create the following trees:
    #
    # Binary tree:
    #
    #          A
    #          ●
    #        /   \
    #      B       C
    #      ●       ●
    #    /   \   /   \
    #   D     E F     G
    #   ●     ● ●     ●
    #
    # Binary search tree:
    #
    #          4
    #          ●
    #        /   \
    #      2       6
    #      ●       ●
    #    /   \   /   \
    #   1     3 5     7
    #   ●     ● ●     ●

    def setUp(self):
        # Create nodes for binary tree
        self.node_A = TreeNode(value="A")
        self.node_B = TreeNode(value="B")
        self.node_C = TreeNode(value="C")
        self.node_D = TreeNode(value="D")
        self.node_E = TreeNode(value="E")
        self.node_F = TreeNode(value="F")
        self.node_G = TreeNode(value="G")

        # Set up parent relationships for binary tree
        self.node_B.parent, self.node_C.parent = self.node_A, self.node_A
        self.node_D.parent, self.node_E.parent = self.node_B, self.node_B
        self.node_F.parent, self.node_G.parent = self.node_C, self.node_C

        # Set up child relationships for binary tree
        self.node_A.left, self.node_A.right = self.node_B, self.node_C
        self.node_B.left, self.node_B.right = self.node_D, self.node_E
        self.node_C.left, self.node_C.right = self.node_F, self.node_G

        # Set root node for binary tree
        self.root = self.node_A

        # Create nodes for binary search tree
        self.node_1 = TreeNode(value=1)
        self.node_2 = TreeNode(value=2)
        self.node_3 = TreeNode(value=3)
        self.node_4 = TreeNode(value=4)
        self.node_5 = TreeNode(value=5)
        self.node_6 = TreeNode(value=6)
        self.node_7 = TreeNode(value=7)

        # Set up parent relationships for binary search tree
        self.node_2.parent, self.node_6.parent = self.node_4, self.node_4
        self.node_1.parent, self.node_3.parent = self.node_2, self.node_2
        self.node_5.parent, self.node_7.parent = self.node_6, self.node_6

        # Set up child relationships for binary search tree
        self.node_4.left, self.node_4.right = self.node_2, self.node_6
        self.node_2.left, self.node_2.right = self.node_1, self.node_3
        self.node_6.left, self.node_6.right = self.node_5, self.node_7

        # Set root node for binary search tree
        self.bst_root = self.node_4

    def test_depth_first_search(self):
        exp = ["A", "B", "D", "E", "C", "F", "G"]
        assert tree_operations.depth_first_search(self.root) == exp

    def test_breadth_first_search(self):
        exp = ["A", "B", "C", "D", "E", "F", "G"]
        assert tree_operations.breadth_first_search(self.root) == exp

    def test_tree_size(self):
        exp = 7
        assert tree_operations.tree_size(self.root) == exp

    def test_tree_height(self):
        exp = 2
        assert tree_operations.tree_height(self.root) == exp

    def test_bst_search_recursive_present(self):
        exp = self.node_7
        assert tree_operations.bst_search_recursive(self.bst_root, 7) == exp

    def test_bst_search_recursive_not_present(self):
        exp = None
        assert tree_operations.bst_search_recursive(self.bst_root, 1337) == exp

    def test_bst_search_iterative_present(self):
        exp = self.node_7
        assert tree_operations.bst_search_iterative(self.bst_root, 7) == exp

    def test_bst_search_iterative_not_present(self):
        exp = None
        assert tree_operations.bst_search_iterative(self.bst_root, 1337) == exp

    def test_bst_min(self):
        exp = self.node_1
        assert tree_operations.bst_min(self.bst_root) == exp

    def test_bst_max(self):
        exp = self.node_7
        assert tree_operations.bst_max(self.bst_root) == exp

    def test_bst_successor(self):
        exp = self.node_5
        assert tree_operations.bst_successor(self.bst_root) == exp

    def test_bst_predecessor(self):
        exp = self.node_3
        assert tree_operations.bst_predecessor(self.bst_root) == exp

    def test_bst_insert(self):
        """
        Tests both `bst_insert_recursive()` and `bst_insert_iterative()`.
        """
        # Binary search tree:
        #
        #        3               3
        #        ●               ●
        #      /   \           /   \
        #     1      5        1      5
        #     ●      ●        ●      ●
        #                          /   \
        #                         4     6
        #                         ●     ●
        #
        # Insert 4 and 6

        # Create nodes for binary search tree
        self.node_1 = TreeNode(value=1)
        self.node_3 = TreeNode(value=3)
        self.node_5 = TreeNode(value=5)

        # Set up parent relationships for binary search tree
        self.node_1.parent, self.node_5.parent = self.node_3, self.node_3

        # Set up child relationships for binary search tree
        self.node_3.left, self.node_3.right = self.node_1, self.node_5

        # Set root node for binary search tree
        self.bst_root = self.node_3

        exp = [3, 1, 5, None, None, 4, 6]
        assert tree_operations.bst_insert_recursive(self.node_3, 4).value == 4
        assert tree_operations.bst_insert_iterative(self.node_3, 6).value == 6
        assert_tree(self.bst_root, exp)

    def test_bst_delete(self):
        # Binary search tree:
        #
        #        3            3           3
        #        ●            ●           ●
        #      /   \        /   \       /   \
        #     1      5     1     6     1     6
        #     ●      ●     ●     ●     ●     ●
        #          /   \
        #         4     6
        #         ●     ●
        #
        # Remove 5 and 4, then remove 3 (root).

        # Create nodes for binary search tree
        self.Node_1 = TreeNode(value=1)
        self.Node_3 = TreeNode(value=3)
        self.Node_4 = TreeNode(value=4)
        self.Node_5 = TreeNode(value=5)
        self.Node_6 = TreeNode(value=6)

        # Set up parent relationships for binary search tree
        self.Node_1.parent, self.Node_5.parent = self.Node_3, self.Node_3
        self.Node_4.parent, self.Node_6.parent = self.Node_5, self.Node_5

        # Set up child relationships for binary search tree
        self.Node_3.left, self.Node_3.right = self.Node_1, self.Node_5
        self.Node_5.left, self.Node_5.right = self.Node_4, self.Node_6

        # Set root node for binary search tree
        self.bst_root = self.Node_3

        exp = [3, 1, 6]
        root = self.bst_root
        root = tree_operations.bst_delete(root, 5)
        root = tree_operations.bst_delete(root, 4)
        assert_tree(self.bst_root, exp)
        exp = [6, 1]
        root = tree_operations.bst_delete(self.Node_3, 3)
        assert_tree(root, [6, 1])
