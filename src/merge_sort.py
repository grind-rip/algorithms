"""
Merge Sort
----------

Merge sort is the quintessential divide-and-conquer sorting algorithm. It
follows the premise that an array of one element is considered sorted.
Furthermore, it is trivial to sort two sorted arrays.

The algorithm can be stated as follows:
  1. Divide the unsorted list into n sublists, each containing one element (a
     list of one element is considered sorted).
  2. Repeatedly merge sublists to produce new sorted sublists until there is
     only one sublist remaining. This will be the sorted list.

Time Complexity: O(nlog n)
Space Complexity: O(n)

Counting Inversions
-------------------
The merge sort algorithm can be extend to count the number of inversions
required to sort an unsorted array. Counting inversions tells us how "unsorted"
an array is - it's the minimum number of adjacent swaps needed to sort the
array. The key insight is that during the merge step, when we take an element
from the right array (i.e., l1[i] > l2[j]), it represents inversions with all
remaining elements in the left array.
"""


def merge_sort(l: list[int]) -> list[int]:
    """
    Top-down implementation of merge sort.
    """
    if not l:
        return l
    mid = len(l) // 2
    return merge(merge_sort(l[:mid]), merge_sort(l[mid:]))


def merge(l1: list[int], l2: list[int]) -> list[int]:
    l3: list[int] = []  # Sorted list
    i, j = 0, 0
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            l3.append(l1[i])
            i += 1
        else:
            # If counting inversions, increment inversion count by
            # len(left) - i. This represents inversions with all remaining
            # elements in the left array:
            #
            #   inversions += len(left) - i
            l3.append(l2[j])
            j += 1

    while i < len(l1):
        l3.append(l1[i])
        i += 1

    while j < len(l2):
        l3.append(l2[j])
        j += 1

    return l3
