"""
kth Smallest (Largest)
----------------------
"""

import random
from unittest import TestCase

from src.kth_smallest import kth_smallest


class TestKthSmallest(TestCase):
    def test_kth_smallest(self):
        # Pick a 'k' within the range of 'l' [1:n], inclusive. k cannot be 0. k
        # represents the kth element in a one-based array. To get the kth
        # element for a zero-based array, use k - 1.
        n = random.randint(1, 10)
        k = random.randint(1, n)
        l = [random.randint(-10, 10) for _ in range(n)]
        exp = sorted(l.copy())[k - 1]
        assert kth_smallest(l, k) == exp
