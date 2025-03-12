"""
Longest Common Substring
------------------------

The longest common substring is the longest substring that is common to two or
more strings. It can be found using a dynamic programming approach.

Definitions:
  * Substring: A contiguous sequence of characters that can be derived from
    another string.

Dynamic programming
-------------------
The dynamic programming solution is similar to the Longest Common Subsequence
solution, however, since substrings are inherently simpler than subsequences, the
implementation is also simpler.

We use a 2D array, dp, to store the length of the longest common suffix
(substring) of the prefixes a[0...i] and b[0...j], where i and j are the end
positions of the substrings for each respective string.

As with most dynamic programming problems, we define our base cases:

  1. If the length of `a` or `b` is 0, then the longest common substring has
     length 0.

  2. If a[i] == b[j], then the longest common substring is *at least* 1.
     However, if a[i - 1] and b[j - 1] denote the last characters of a common
     substring, use its length. This is represented programmatically with the
     following:

       dp[i][j] = dp[i-1][j-1] + 1

The longest common substrings are represented by the maximum values in dp
located at the end positions for the substrings in `a` and `b`.

Unlike with the Longest Common Subsequence algorithm, the 2D array does not
build to a solution at dp[i][j]. Therefore, the length and indices of the
longest common substrings are maintained while iterating.

The dynamic programming approach has O(n x m) time complexity, however, with
the help of a generalized suffix tree, the time complexity is reduced to
O(n + m).

Suffix tree
-----------
"""


def longest_common_substring(a: str, b: str) -> list[str]:
    """
    Given two strings, `a` and `b`, return their longest common substrings.
    """
    # Length of the longest common substrings.
    longest = 0
    # Indices of the last character of the longest common substrings.
    longest_idxs: set[int] = set()

    # Create an m×n matrix initialized to 0s, where m is the number of rows
    # (|a|) and n is the number of columns (|b|).
    m, n = len(a), len(b)
    dp: list[list[int]] = [[0 for j in range(n)] for i in range(m)]

    # Fill the remaining matrix for all remaining suffixes (substrings). For
    # each position dp[i][j], we calculate:
    #
    #   If a[i] == b[j], dp[i][j] = dp[i-1][j-1] + 1
    #
    # This means we include the current matching character and add 1 to the
    # previous longest common substring length.
    #
    #   Else, dp[i][j] = 0
    #
    # Otherwise, since a substring must be contiguous, we set value to 0.
    for i in range(m):
        for j in range(n):
            if a[i] == b[j]:
                # NOTE: Since the solution to the current subproblem builds
                # from the solution to the previous subproblem, it is common to
                # initialize the 2D array to be m + 1 and n + 1, then iterate
                # from dp[1...m][1...n]. This, however, requires that the
                # indices into `a` and `b` be different from the indices into
                # dp for `i` and `j`. Instead, we can simply handle the edge
                # case with a conditional and set the value accordingly.
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > longest:
                    longest = dp[i][j]
                    longest_idxs = {i}
                elif dp[i][j] == longest:
                    longest_idxs.add(i)
            else:
                dp[i][j] = 0

    ret: list[str] = []
    for i in longest_idxs:
        ret.append(a[i - longest + 1 : i + 1])

    return ret
