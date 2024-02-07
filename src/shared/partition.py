"""
The `partition` function (in linear time) groups a list (ranging from indices
'left' to 'right') into two parts: those less than a certain element, and those
greater than or equal to the element.

This implementation uses the Lomuto partition scheme, which chooses as the
pivot the last element in the array.

  2 1 4 6 3 5
            ^
The algorithm maintains index i as it scans the array using another index j
such that the elements at lo through i-1 (inclusive) are less than the pivot,
and the elements at i through j (inclusive) are equal to or greater than the
pivot.

It is used in both the quickselect and quicksort algorithms.
"""

from typing import List


def partition(l: List[int], left: int, right: int) -> int:
    """
    Reorder the list such that elements less than the pivot are before elements
    greater than or equal to the pivot. When complete, the pivot is in its
    final sorted position. The pivot is always the last element in the list
    (Lomuto partition scheme).

    NOTE: We cannot simply use a slice of a list, since rearranging the
    elements in the slice will not reorder the elements in the original list.
    """

    def swap(l: List[int], i: int, j: int) -> None:
        """
        Swaps the element at index i with the element at index j.
        """
        temp = l[j]
        l[j] = l[i]
        l[i] = temp

    # Choose the last element (right) as the pivot.
    pivot = l[right]

    # i (commonly referred to as the "store index") is used to denote the index
    # of the pivot. j is used for scanning the list from `left` to `right - 1`.
    i, j = left, left

    # The loop maintains the following invariant:
    #
    #   Elements 'left' through i-1 (inclusive) are less than 'pivot'
    #   Elements 'i' through j (inclusive) are greater than or equal to 'pivot'
    while j < right:
        if l[j] < pivot:
            swap(l, i, j)
            i += 1
        j += 1

    # As a final step, move pivot to its final position. This will be its final
    # position in the sorted array.
    swap(l, i, right)

    # Return the index of the pivot. The pivot index can be used to determine
    # the new 'left' and 'right' arguments for quicksort or can be used to
    # determine the k-th element in a list.
    return i
