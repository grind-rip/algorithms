from unittest import TestCase

from src.shared.node import Node


class TestNode(TestCase):
    def test(self):
        n = Node(0)
        assert isinstance(n, Node)
