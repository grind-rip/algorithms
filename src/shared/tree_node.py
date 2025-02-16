from typing import Generic, Protocol, TypeVar


class Comparable(Protocol):
    """
    Defines a protocol for comparable types.
    """

    def __gt__(self, other) -> bool: ...

    def __lt__(self, other) -> bool: ...


# TypeVar bound to Comparable
T = TypeVar("T", bound=Comparable)


class TreeNode(Generic[T]):
    """
    A tree node with a value of type 'T'.
    """

    def __init__(self, value: T) -> None:
        self.value: T = value
        self.parent: TreeNode[T] | None = None
        self.left: TreeNode[T] | None = None
        self.right: TreeNode[T] | None = None
