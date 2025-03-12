"""
Levenshtein Distance
--------------------

Levenshtein distance is a string metric for measuring the difference between
two sequences. The Levenshtein distance between two words is the minimum number
of single-character edits (insertions, deletions, or substitutions) required to
change one word into the other.

The Levenshtein distance (lev(a,b)) between two strings, `a` and `b`, is
calculated as follows:

  * If |b| = 0, then |a|
  * If |a| = 0, then |b|
  * If head(a) = head(b), then lev(tail(a), tail(b))
  * Else 1 + the minimum of:
    * lev(tail(a),b), representing a deletion from `a`
    * lev(a,tail(b)), representing an insertion into `a`
    * lev(tail(a),tail(b)), representing a substitution from `b` to `a`

Where |a| is the length of `a` and |b| is the length of `b`. `head` is the
first character in the string. `tail` is a string of all but the first
character.

* Insertion: Adds a character to the end
* Deletion: Removes a character from the end
* Substitution: Replaces a character at any position

We find that this problem is amenable to dynamic programming, using either
tabularization or memoization, since its solution can be constructed
efficiently from optimal solutions of its subproblems:

  >The Levenshtein distance of all possible suffixes can be computed using the
   distance between the last i characters of string `a` and the last j
   characters of string `b`.

     j →
   i     -  a   c   e
   ↓  -  0  1   2   3
      a  1  0   1   2
      b  2  1   1   2
      c  3  2   1   2
      d  4  3   2   2
      e  5  4   3   2

Computing the Levenshtein distance is based on the observation that if we
reserve a matrix to hold the Levenshtein distances between all prefixes of the
first string and all prefixes of the second, then we can compute the values in
the matrix in a dynamic programming fashion, and thus find the distance between
the two full strings as the last value computed.

One thing to note is that the final matrix is the result of *all* previous
calculations, which is essentially an overlay after calculating all possible
suffixes.

Approximate string matching
---------------------------
By initializing the first row of the matrix with zeros (i.e., removing the case
in which the search string is empty), we obtain a variant of the Wagner–Fischer
algorithm that can be used for fuzzy string search of a string in a text. This
modification gives the end-position of matching substrings of the text. To
determine the start-position of the matching substrings, the number of
insertions and deletions can be stored separately and used to compute the
start-position from the end-position.
"""


def levenshtein_distance(a: str, b: str) -> int:
    """
    Uses the Wagner–Fischer algorithm, a dynamic programming algorithm that
    computes the edit distance between two strings of characters, to calculate
    the Levenshtein distance between `a` and `b`.

    It is important to note that the input strings are indexed using i-1 and
    j-1, while the matrix is indexed using i and j.
    """
    # Create an m x n matrix initialized to 0s.
    #
    #   [0, 0, 0, 0]
    #   [0, 0, 0, 0]
    #   [0, 0, 0, 0]
    #   [0, 0, 0, 0]
    #   [0, 0, 0, 0]
    #   [0, 0, 0, 0]
    #
    # where m is the number of rows (|a| + 1) and n is the number of columns
    # (|b| + 1).
    m, n = len(a) + 1, len(b) + 1
    dp: list[list[int]] = [[0 for j in range(n)] for i in range(m)]

    # Set dp[0...m, 0] to i, the cost of deleting all characters from `a`. This
    # is equivalent to comparing `a` to an empty string, which is our first
    # assertion from above:
    #
    #   If |b| = 0, then |a|
    for i in range(m):
        dp[i][0] = i

    # Set dp[0, 0...n] to j, the cost of inserting all characters into `a`.
    # This is equivalent to comparing `b` to an empty string, which is our
    # second assertion from above:
    #
    #   If |a| = 0, then |b|
    for j in range(n):
        dp[0][j] = j

    # Our matrix now has the following values:
    #
    #   [0, 1, 2, 3]
    #   [1, 0, 0, 0]
    #   [2, 0, 0, 0]
    #   [3, 0, 0, 0]
    #   [4, 0, 0, 0]
    #   [5, 0, 0, 0]

    # Fill the remaining matrix for all remaining prefixes. For each index in
    # dp[i][j], we make the following calculation:
    #
    # If a[i-1] == b[i-1], dp[i][j] = dp[i-1][j-1] (diagonal). This is
    # equivalent to our third assertion from above:
    #
    #   If head(a) = head(b), then lev(tail(a), tail(b))
    #
    # Else, we take the minimum of the following:
    #   * Deletion:     dp[i][j] = dp[i-1][j] + 1    (top)
    #   * Insertion:    dp[i][j] = dp[i][j-1] + 1    (left)
    #   * Substitution: dp[i][j] = dp[i-1][j-1] + 1  (diagonal)
    for i in range(1, m):
        for j in range(1, n):
            if a[i - 1] == b[i - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(
                    dp[i - 1][j] + 1,  # deletion
                    dp[i][j - 1] + 1,  # insertion
                    dp[i - 1][j - 1] + 1,  # substitution
                )

    return dp[i][j]
