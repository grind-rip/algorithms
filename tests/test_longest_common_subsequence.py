"""
Longest Common Subsequence (LCS)
--------------------------------
"""

from src.longest_common_subsequence import longest_common_subsequence


def test_longest_common_subsequence():
    # Example from Wikipedia.
    assert longest_common_subsequence("ABCD", "ACBAD") == 3

    # Example from a technical assessment.
    assert longest_common_subsequence("...plays under the moon", "sun") == 3
