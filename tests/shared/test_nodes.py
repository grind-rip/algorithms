from unittest import TestCase

from src.shared.nodes import Node, TreeNode


class TestNode(TestCase):
    def test(self):
        n = Node(0)
        assert isinstance(n, Node)


class TestTreeNode(TestCase):
    def test(self):
        t = TreeNode(0)
        assert isinstance(t, TreeNode)
