from typing import Generic, Protocol, TypeVar


class Comparable(Protocol):
    """
    Defines a protocol for comparable types.
    """

    def __gt__(self, other) -> bool: ...

    def __lt__(self, other) -> bool: ...


# TypeVar bound to Comparable
T = TypeVar("T", bound=Comparable)


class Node(Generic[T]):
    """
    A generic node with a value of type 'T'.
    """

    def __init__(self, value: T) -> None:
        self.value: T = value
        self.parent: Node[T] | None = None
        self.children: list[Node[T]] = []
