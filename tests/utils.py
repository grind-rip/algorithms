"""
Utility functions for testing.
"""

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
