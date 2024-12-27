from typing import Generic, TypeVar

T = TypeVar("T")


class Node(Generic[T]):
    """
    A generic node with a value of type 'T'.
    """

    def __init__(self, value: T) -> None:
        self.value: T = value
        self.visited: bool = False
        self.parent: Node[T] | None = None
        self.children: list[Node[T]] = []
