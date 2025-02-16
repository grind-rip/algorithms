from unittest import TestCase

from src.shared.tree_node import TreeNode


class TestTreeNode(TestCase):
    def test(self):
        t = TreeNode(0)
        assert isinstance(t, TreeNode)
