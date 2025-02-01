"""
k-way Merge
-----------
"""

import itertools
import random
from unittest import TestCase

from src.k_way_merge import k_way_merge


class TestKWayMerge(TestCase):
    def test(self):
        """
        Test with `k` randomly generated lists.
        """
        k = random.randint(0, 1000)
        n = random.randint(0, 1000)
        iterables = [sorted([random.randint(-1000, 1000) for _ in range(n)]) for _ in range(k)]
        exp = sorted(itertools.chain(*iterables.copy()))
        assert list(k_way_merge(*iterables)) == exp
