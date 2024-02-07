"""
Quickselect
-----------

Quickselect (also known as Hoare's selection algorithm) is a selection
algorithm to find the kth smallest (or largest) element in an unordered list of
n elements.

Quickselect uses the same overall approach as quicksort, choosing one element
as a pivot and partitioning the data in two based on the pivot, accordingly as
less than or greater than the pivot. However, instead of recursing into both
sides, as in quicksort, quickselect only recurses into one side – the side with
the element it is searching for. This reduces the average complexity from
O(nlog n) to O(n), with a worst case of O(n^2).
"""

from typing import List

from .shared.partition import partition


def quickselect(l: List[int], left: int, right: int, k: int) -> int:
    """
    Return the k-th element in the given list.
    """
    if left == right:
        return l[left]

    # Retrieve the index of the pivot by paritioning the list into elements
    # less than and greater than or equal to the pivot.
    pivot = partition(l, left, right)

    # If k is equal to 'pivot', then 'pivot' is the k-th element in the list.
    # Otherwise, execute quickselect on the parition comprising elments less
    # then or greater than or equal to k.
    if k == pivot:
        return l[k]
    elif k < pivot:
        return quickselect(l, left, pivot - 1, k)
    else:
        return quickselect(l, pivot + 1, right, k)
