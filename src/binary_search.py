"""
Binary Search
-------------

Binary search is an efficient algorithm for finding a target value in a sorted
array. It works by comparing the target value to the middle element of the
array. If they are not equal, the half in which the target cannot reside is
eliminated and the search continues on the remaining half, again taking the
middle element of the array and comparing it to the target value. The process
is repeated until the target value is found. If the search ends with the
remaining half being empty, the target is not in the array.

Binary search runs in logarithmic time in the worst case, making O(log n)
comparisons, where n is the number of elements in the array.
"""


def binary_search(l: list[int], target: int) -> int:
    """
    Return the index of the target value. If the target value is not in the
    list, return -1.

    This implementation uses an iterative approach rather than recursive, as
    it avoids the overhead of recursion. When using the recursive approach, it
    is important to note that the original list must be passed to the recursive
    function along with the target and left and right indices.
    """
    left, right = 0, len(l) - 1

    while left <= right:
        mid = (left + right) // 2
        if target == l[mid]:
            return mid
        elif target < l[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return -1
