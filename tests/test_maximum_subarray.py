"""
Maximum Subarray
----------------
"""

from src.maximum_subarray import maximum_subarray


def test_maximum_subarray():
    exp = 6
    assert maximum_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == exp
