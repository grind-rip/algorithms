"""
Heapsort
--------

Heapsort is a sorting algorithm that first reorganizes an input array into a
heap, then repeatedly removes the largest node from that heap, placing it at
the end of the array.

The heapsort algorithm can be divided into two phases:

  1. Heap construction (also known as heapification)
  2. Heap extraction

Heap construction is the process of converting the array to a binary heap,
specifically a max-heap. The largest value is stored at index 0 (or root) and
each node, i, is greater than or equal to both of its children located at the
following indices:

  * left   = 2*i + 1
  * right  = 2*i + 2
  * parent = (i−1) / 2

Indeed, the formal definition of a heap is an array for which a[i] <= a[2*i+1]
and a[i] <= a[2*i+2] for all i for zero-based arrays. a[0] is always the
smallest element (or largest for max-heaps).

NOTE: Commonly, implementations of heaps store the smallest node at index 0.
This is referred to as a min-heap as opposed to a max-heap, which stores the
largest node at index 0. In general, heaps are min-heaps, however, the heapsort
algorithm uses a max-heap.

NOTE: It can sometimes be confusing when conceptualizing heaps as both binary
trees and arrays. In many cases the terms index 0, a[0], and root are used
interchangeably in reference to the smallest (or largest for max-heaps) value
in the heap.

During heap extraction the heap is converted to a sorted array by repeatedly
removing the largest element from the heap (the root of the heap), and placing
it at the end of the array. The heap is updated after each removal to maintain
the heap property, also called the heap invariant (our formal definition
above). Once all objects have been removed from the heap, the result is a
sorted array. In some implementations, all but *one* object is removed from the
heap, since the last object in the heap is the smallest element in the array,
making the final swap implicit. For completeness, this implementation executes
the final swap.

In-place algorithm
------------------
Heapsort is an in-place algorithm, which makes it particularly concise and
elegant to implement. During the first phase, the array is divided into an
unsorted prefix and a heap-ordered suffix (initially empty). Each step shrinks
the prefix and expands the suffix. When the prefix is empty, this phase is
complete. During the second phase, the array is divided into a heap-ordered
prefix and a sorted suffix (initially empty). Each step shrinks the prefix and
expands the suffix. When the prefix is empty, the array is sorted.

Why is bottom-up heapification O(n)?
------------------------------------
At first glance, it may seem counterintuitive that heapification requires only
O(n) operations. We must process n/2 nodes (all non-leaf nodes) each requiring
in the worst-case O(log n) comparisons resulting in O(nlog n) operations.
However, on closer inspection we find that the number of operations forms a
geometric series that sums to 1.

Given the following insight:

  >Nodes at different levels have different maximum sift distances

The maximum number of operations for node heights in the heap are:
  * Height = 1: n/4  nodes × 1 operations
  * Height = 2: n/8  nodes × 2 operations
  * Height = 3: n/16 nodes × 3 operations

  ...which continues until height = log n

This forms a geometric series:
   n/4 * 1 + n/8 * 2 + n/16 * 3 + ... + 1 * log n

Solving this series results in O(n), not O(nlog n)!

The intuition is that while the root might need log n operations, there are
very few nodes near the root. Most nodes are near the bottom and need very few
operations, which balances out to linear time overall. If we were to build the
heap from the top-down, that is, inserting elements one by one, and sifting
them up to their correct position in the heap, the time complexity would be
O(nlog n) (log(n) comparisons/swaps for n elements). For this reason,
heapification is always done from bottom-up.
"""


def heapsort(l: list[int]) -> list[int]:
    """
    Implementation of heapsort.

    The heapsort algorithm begins by rearranging the array into a binary
    max-heap. The algorithm then repeatedly swaps the root of the heap (the
    largest element in the heap) with the last element in the heap, thereby
    extending the sorted prefix. The swap, however, causes the heap to violate
    the heap invariant. Sifting the new root down to its correct position in
    the heap restores the heap invariant, placing the largest element again in
    the root position. This process repeats until the heap is empty. The final
    swap is considered implicit.
    """
    # Build the heap from the array.
    _heapify(l)

    i = len(l) - 1
    while i >= 0:  # For completeness, execute the final swap.
        # Swap the root, the largest element in the heap, with the element at
        # index i. Since the heap may now violate the heap invariant, sift the
        # element (the new root) down to its correct position. Reduce the range
        # of the heap by 1.
        l[0], l[i] = l[i], l[0]
        _sift_down(l, 0, i)
        i -= 1

    return l


def _heapify(l: list[int]) -> None:
    """
    Build a binary max-heap from an array.

    Heapify (or bottom-up heapification) is the process of converting an array
    into a heap. Starting with the first non-leaf node (i.e., the parent of the
    last element in the array), nodes are sifted down the heap until they
    satisfy the heap invariant. This implementation starts with the last node,
    which is a leaf node. Since a leaf node satisfies the heap property, this
    is unnecessary. To optimize this implementation, we would use the parent of
    the last element in the array, which would reduce the number of operations
    by half (n → n/2).
    """
    i = len(l) - 1
    while i >= 0:  # For completeness, execute the final sift down.
        _sift_down(l, i, len(l))
        i -= 1


def _sift_down(l: list[int], i: int, n: int) -> None:
    """
    The heart of the heapsort algorithm (and heaps in general) is the "sift
    down" function. The sift down function moves node i to a position that
    satisfies the heap property by satisfying one of three cases:

      1. The node has no children (i.e., it is a leaf node).
      2. The node is greater than or equal to both its children.
      3. The node is less than the greatest child and the nodes are exchanged.

    The third case may violate the heap property for subtree for which the node
    is now the root. Therefore the sift down operation is repeated. In this
    way, smaller nodes are "sifted down" and as a side effect larger nodes are
    moved up to take their place.

    By calling the sift down function on n/2 nodes (all non-leaf), a heap is
    formed from the array.
    """
    # Keep swapping the parent node with its largest child until it is the
    # largest of its children or is a leaf node.
    while True:
        # If the node has no children (i.e., it is a leaf node), it cannot be
        # sifted down any further.
        if _is_leaf(i, n):
            break
        left, right = _left_child(i), _right_child(i)
        # To establish the max-heap property at i, up to three nodes must be
        # compared (the root and one or both of its children). The largest is
        # swapped with i. If i is the largest node, the heap invariant is
        # satisfied and no swap occurs.
        largest = i
        if left < n and l[left] > l[largest]:
            largest = left
        if right < n and l[right] > l[largest]:
            largest = right
        if largest != i:
            l[i], l[largest] = l[largest], l[i]
            i = largest
        else:
            break


def _left_child(i: int) -> int:
    """
    The left child of a node at index i in zero-based array is given by 2*i+1.
    """
    return 2 * i + 1


def _right_child(i: int) -> int:
    """
    The right child of a node at index i in zero-based array is given by 2*i+2.
    """
    return 2 * i + 2


def _parent(i: int) -> int:
    """
    The parent of a node at index i in zero-based array is given by (i-1)/2.
    """
    return (i - 1) // 2


def _is_leaf(i: int, n: int) -> bool:
    """
    For a complete binary tree represented by a zero-based array of length n,
    the first leaf node is at position n/2. If the node at index i is greater
    or equal to n/2, it is a leaf node.
    """
    return i >= n // 2


def heapsort_optimized(l: list[int]) -> list[int]:
    """
    Optimized implementation of heapsort.
      * Does not execute the final swap.
    """
    _heapify_optimized(l)

    i = len(l) - 1
    while i > 0:
        l[0], l[i] = l[i], l[0]
        _sift_down_optimized(l, 0, i)
        i -= 1

    return l


def _heapify_optimized(l: list[int]) -> None:
    """
    Optimized heapify function.
      * Starts with the first non-leaf node.
    """
    i = _parent(len(l) - 1)
    while i >= 0:
        _sift_down_optimized(l, i, len(l))
        i -= 1


def _sift_down_optimized(l: list[int], i: int, n: int) -> None:
    """
    Optimized sift down function.
      * Implicitly checks if the node is a leaf node.
    """
    while True:
        left, right = _left_child(i), _right_child(i)
        largest = i
        if left < n and l[left] > l[largest]:
            largest = left
        if right < n and l[right] > l[largest]:
            largest = right
        if largest != i:
            l[i], l[largest] = l[largest], l[i]
            i = largest
        else:
            break
