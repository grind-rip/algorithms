"""
Heapsort
--------
"""

import random
from unittest import TestCase

from src.heapsort import heapsort, heapsort_optimized


class TestHeapsort(TestCase):
    def test(self):
        """
        Test with 100 randomly generated lists.
        """
        for _ in range(100):
            n = random.randint(0, 1000)
            l = [random.randint(-1000, 1000) for _ in range(n)]
            exp = sorted(l)
            # NOTE: Both heapsort implementations modify the list in-place, so
            # a copy of the list is made.
            assert heapsort(l.copy()) == exp
            assert heapsort_optimized(l.copy()) == exp
