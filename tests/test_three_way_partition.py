"""
Three-way Partition
-------------------
"""

import random
from unittest import TestCase

from src.three_way_partition import three_way_partition


class TestThreeWayPartition(TestCase):
    def test(self):
        exp = [0, 0, 0, 1, 1, 1, 2, 2, 2]
        arr = [0, 0, 0, 1, 1, 1, 2, 2, 2]
        random.shuffle(arr)
        assert arr != exp
        three_way_partition(arr, 1)
        assert arr == exp
