"""
Longest Increasing Subsequence (LIS)
------------------------------------

The longest increasing subsequence is the longest sequence of numbers from an
array where each number is greater than the previous one. It can be found using
a dynamic programming approach.

The algorithm is fairly straight-forward. Given an array of elements, A, we
maintain an array, dp, of the longest increasing subsequence ending at index i.

  dp[i] is equivalent to LIS(A[0]...A[i]) for all `n`

For each element in A[1...n], we calculate the LIS, LIS(A[0]...A[i]), by taking
the maximum of dp[i], the current LIS for position i, or dp[j] + 1, the current
LIS for position j plus 1, only if A[i] > A[j].

Put more simply, the longest increasing subsequence is the longest increasing
subsequence with or without the addition of the current element under
consideration.

The time complexity is O(n^2) where n is the length of the array, however
there's also a more efficient O(nlog n) solution using binary search.
"""


def lis(nums: list[int]) -> int:
    """
    Given an array of integers compute the length of its Longest Increasing
    Subsequence (LIS).
    """
    if not nums:
        return 0

    # dp[i] represents the length of the LIS ending at index i. The array is
    # initialized to 1s, since each integer is itself an increasing
    # subsequence.
    dp: list[int] = [1] * len(nums)

    # For each position, look at all previous positions
    for i in range(1, len(nums)):
        for j in range(i):
            # If we can extend the sequence
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)
