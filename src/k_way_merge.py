"""
k-way Merge
-----------

The k-way merge algorithm is a sequence merge algorithm that takes in k sorted
lists, typically greater than two, and merges them into a single sorted list.
It can be efficiently solved in O(nlog k) time using a heap, where n is the
total number of elements for all k lists.

First, a heap is built using the first element of each list. Given that bottom-
up heapification can be done in linear time, this has O(k) time complexity.
Next, the smallest element is retrieved from the heap and the next element from
the list from which the element was taken is inserted into the heap. This
process continues until the heap is empty.
"""

from collections.abc import Iterable, Iterator
from heapq import heapify, heappop, heapreplace
from typing import Protocol, TypeVar


class Comparable(Protocol):
    """
    Defines a protocol for comparable types.
    """

    def __lt__(self, other) -> bool: ...


# Create a TypeVar bound to Comparable
T = TypeVar("T", bound=Comparable)


def k_way_merge(*iterables: Iterable[T]) -> Iterator[T]:
    """
    k-way merge is a merge algorithm that, as the name suggests, merges k
    sorted lists into a single sorted list. It can be efficiently solved in
    O(nlog k) using a heap.
    """
    # Build a heap using the first element of each list. The generator and
    # iterator pattern is used to keep track of the "head" of each list. This
    # is a very elegant solution, which I stole from the original heapq
    # implementation. Basically, a node in the heap contains its value and its
    # next value, similar to a linked list. Each node has an additional "index"
    # that associates it with an iterable. This is required to resolve tuple
    # comparisons where the values of nodes are the same. When Python compares
    # tuples, it compares elements in order until it finds a difference. Using
    # an index, a node from list with a lower index will take precedence over a
    # node with a higher index.
    heap: list[tuple[T, int, Iterator[T]]] = []
    for i, it in enumerate(map(iter, iterables)):
        try:
            e = next(it)
            heap.append((e, i, it))
        except StopIteration:
            pass
    heapify(heap)

    # For each selection, we retrieve the smallest element from the heap
    # (heap[0]), which contains a value and an iterator. The value is yielded,
    # and a new value is retrieved from the iterator with a call to `next()`.
    # The root node is removed from the heap and replaced with the next element
    # from the list from which the node was taken. If `next()` raises a
    # StopIteration exception, the iterator has been exhausted meaning the
    # previous element was the final element from the iterable. If this is the
    # case, we simply delete the smallest element from the heap.
    while heap:
        try:
            e, i, it = heap[0]
            yield e
            e = next(it)
            heapreplace(heap, (e, i, it))
        except StopIteration:
            heappop(heap)
