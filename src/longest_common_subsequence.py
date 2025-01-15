"""
Longest Common Subsequence (LCS)
--------------------------------

The longest common subsequence is the longest subsequence that is common to two
or more sequences. It can be found using a dynamic programming approach.

Definitions:
  * Sequence: An ordered list of elements where the order matters.
  * Subsequence: A sequence that can be derived from another sequence by
    deleting some or no elements without changing the order of the remaining
    elements.

The length of the Longest Common Subsequence (LCS(a,b)) between two strings,
`a` and `b`, is calculated as follows:

  * If |a| = 0 or |b| = 0, then 0
  * If a[i] = b[j], then 1 + LCS(a[:i], b[:j])
  * Else the maximum of:
    * LCS(a[:i], b), exclude the character at position i in `a`
    * LCS(a, b[:j]), exclude the character at position j in `b`

Where |a| is the length of `a` and |b| is the length of `b`.

Formally, given two sequences, X and Y, and prefixes of X and Y, Xi and Yi, to
find the LCS of Xi and Yj (LCS(Xi,Yi)), compare xi and yj, the ith and jth
character in the two sequences. If they are equal, then the previous LCS
(LCS(Xi−1,Yj−1)) is extended by that element. If they are not equal, then the
current LCS is the maximum LCS for the sequences, LCS(Xi,Yj−1) and
LCS(Xi−1,Yj). If the sequences are the same length, but not identical, then
both are retained. The base case, when either Xi or Yi is empty, is an empty
string, ϵ.

From this, we can derive an optimal subproblem:

The longest common subsequence at any position (i,j) is:
  * The previous LCS (at position (i-1,j-1)) plus 1 if the current characters
    are the same
  * Otherwise, the maximum of the LCS when excluding the current character from
    either sequence (positions (i-1,j) or (i,j-1))

Longest Common Subsequence (LCS) is a classic dynamic programming problem. It
has an optimal substructure: the problem can be broken down into smaller,
simpler subproblems, which can, in turn, be broken down into simpler
subproblems, and so on, until, finally, the solution becomes trivial. LCS in
particular has overlapping subproblems: the solutions to high-level subproblems
often reuse solutions to lower level subproblems. Problems with these two
properties are amenable to dynamic programming approaches, in which subproblem
solutions are memoized, that is, the solutions of subproblems are saved for
reuse.

For the case of two sequences of n and m elements, the running time of the
dynamic programming approach is O(n×m).

NOTE: Not to be confused with Longest Common Subsequence (LCS) distance, which
is the edit distance using only the insertion and deletion edit operations.
"""


def lcs(a: str, b: str) -> int:
    """
    Given two strings, `a` and `b`, compute the length of their Longest Common
    Subsequence (LCS).
    """
    # Create an m×n matrix initialized to 0s, where m is the number of rows
    # (|a| + 1) and n is the number of columns (|b| + 1).
    #
    # dp[0...m, 0] and dp[0, 0...n] are set to 0. This represents our base
    # case:
    #
    #   If either sequence is empty, the LCS length is 0.
    m, n = len(a) + 1, len(b) + 1
    dp: list[list[int]] = [[0 for j in range(n)] for i in range(m)]

    # Fill the remaining matrix for all remaining prefixes. For each position
    # dp[i][j], we calculate:
    #
    #   If a[i-1] == b[j-1], dp[i][j] = 1 + dp[i-1][j-1]
    #
    # This means we include the current matching character and add 1 to the
    # previous LCS length.
    #
    #   Else, dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    #
    # This means we take the maximum LCS length when excluding either the
    # current character from sequence `a` or sequence `b`.
    for i in range(1, m):
        for j in range(1, n):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(
                    dp[i - 1][j],  # exclude the character at position i in `a`
                    dp[i][j - 1],  # exclude the character at position j in `b`
                )

    return dp[i][j]
