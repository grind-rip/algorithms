"""
Utility functions for testing.
"""

from collections import deque

from src.shared.tree_node import T, TreeNode


def assert_tree(root: TreeNode | None, exp: list[T | None]) -> None:
    """
    Given a list of values in level-order traversal, assert that the tree is
    matches the expected values. Gaps in the tree are denoted by None.
    """

    def _assert_tree(root: TreeNode | None, i: int, exp: list[T | None]) -> None:
        """
        Given a list of values in level-order traversal, assert that the tree is
        matches the expected values. Gaps in the tree are denoted by None.
        """
        if not root:
            return None
        assert root.value == exp[i]
        _assert_tree(root.left, 2 * i + 1, exp)
        _assert_tree(root.right, 2 * i + 2, exp)

    _assert_tree(root, 0, exp)


def serialize_binary_tree(root: TreeNode[T] | None) -> list[T | None]:
    """
    Serializes a binary tree similar to LeetCode.
    """
    l: list[T | None] = []

    if not root:
        return l

    q: deque[TreeNode[T] | None] = deque([root])

    while q:
        curr: TreeNode[T] | None = q.popleft()
        if curr:
            l.append(curr.value)
        else:
            l.append(None)
        if curr:
            q.append(curr.left)
            q.append(curr.right)

    # Remove trailing 'None' values.
    while not l[-1]:
        l.pop()

    return l
