"""
Longest Common Substring
------------------------
"""

from unittest import TestCase

from src.longest_common_substring import longest_common_substring


class TestLongestCommonSubstring(TestCase):
    def test(self):
        exp = ["ABC"]
        a, b = "ABABC", "ABCBA"
        assert longest_common_substring(a, b) == exp
