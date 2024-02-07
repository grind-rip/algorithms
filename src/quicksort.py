"""
Quicksort
---------

Quicksort is a divide-and-conquer algorithm. It works by selecting a 'pivot'
element from the array and partitioning the other elements into two sub-arrays,
according to whether they are less than or greater than the pivot. For this
reason, it is sometimes called partition-exchange sort. The sub-arrays are then
sorted recursively. This can be done in-place, requiring small additional
amounts of memory to perform the sorting.
"""

from typing import List

from .shared.partition import partition


def quicksort(l: List[int], left: int, right: int) -> None:
    """
    Sort the given list using the quicksort algorithm.
    """
    if len(l) <= 1:
        return

    # Retrieve the index of the pivot by paritioning the list into elements
    # less than and greater than or equal to the pivot.
    pivot = partition(l, left, right)

    # Recursively sort the two partitions.
    quicksort(l, left, pivot - 1)
    quicksort(l, pivot + 1, right)
