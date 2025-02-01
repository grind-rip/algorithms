"""
kth Smallest (Largest)
----------------------

The kth smallest (or largest) problem can be efficiently solved using a
max-heap (or min-heap). Maintaining a heap of size k, the kth smallest value is
always the root of the max-heap. To retrieve all k smallest elements, simply
return the sorted heap.
"""

from heapq import heapify, heapreplace


def kth_smallest(l: list[int], k: int) -> int:
    """
    The kth smallest (or largest) problem can be efficiently solved using a
    max-heap (or min-heap). Maintaining a heap of size k, the kth smallest
    value is always the root of the max-heap. For all k smallest elements,
    simply return the sorted heap.

    NOTE: The `heapq` module does not expose the `_heapify_max()` function. In
    order to create a max-heap, elements are negated before being added to the
    heap. Additionally, the comparison when determining if the new element
    should be added to the heap is reversed.
    """
    # Build a heap from the first k elements of the list.
    heap: list[int] = []
    for i in range(k):
        heap.append(-l[i])
    heapify(heap)
    # Iterate over the remaining values in the list. If a value is less than
    # the largest value in the heap, replace it.
    for i in range(k, len(l)):
        if -l[i] > heap[0]:
            heapreplace(heap, -l[i])
    return -heap[0]


def kth_largest(l: list[int], k: int) -> int:
    """
    Same as `kth_smallest()`, but for the kth largest value.
    """
    heap: list[int] = []
    for i in range(k):
        heap.append(l[i])
    heapify(heap)
    for i in range(k, len(l)):
        if l[i] > heap[0]:
            heapreplace(heap, l[i])
    return heap[0]
