from typing import Generic, TypeVar

T = TypeVar("T")


class TreeNode(Generic[T]):
    """
    A tree node with a value of type 'T'.
    """

    def __init__(self, value: T) -> None:
        self.value: T = value
        self.parent: TreeNode[T] | None = None
        self.left: TreeNode[T] | None = None
        self.right: TreeNode[T] | None = None
