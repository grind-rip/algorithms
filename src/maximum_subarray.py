"""
Maximum Subarray
----------------

The maximum subarray problem is the task of finding a contiguous subarray with
the largest sum, within a given one-dimensional array A[1...n] of numbers. It
can be solved in O(n) time and O(1) space.

Definitions:
  * A subarray is a contiguous non-empty sequence of elements within an array.

Although this problem can be solved using several different algorithmic
techniques, a simple single-pass algorithm known as Kadane's algorithm solves
it efficiently.

Kadane's Algorithm
------------------
Kadane's algorithm scans the given array A[0...n-1] from left to right. In the
ith step, it computes the subarray with the largest sum ending at i; this sum
is maintained in variable current_sum. Moreover, it computes the subarray with
the largest sum anywhere in A[0...i], maintained in variable max_sum, and
easily obtained as the maximum of all values of current_sum seen so far.

As a loop invariant, in the ith step, the previous value of current_sum holds
the maximum over all elements up to i - 1. Therefore, current_sum + A[i] is the
maximum over all elements up to i provided that A[i] is not greater than
current_sum + A[i]. A[i], or current_sum, now holds the maximum over all
elements up to i.

NOTE: If empty subarrays are admitted, max_sum is initialized to 0 and the
following calculation for current_sum is used:

  current_sum = max(current_sum + x, 0)
"""

import sys


def maximum_subarray(nums: list[int]) -> int:
    current_sum, max_sum = 0, -sys.maxsize
    for x in nums:
        current_sum = max(current_sum + x, x)
        max_sum = max(max_sum, current_sum)
    return max_sum
