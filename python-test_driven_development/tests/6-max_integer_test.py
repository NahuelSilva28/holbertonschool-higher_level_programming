#!/usr/bin/python3
"""test"""

import unittest
max_integer = __import__('6-max_integer').max_integer
"""_summary_
"""


class TestMaxInteger(unittest.TestCase):
    def test_max(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertEqual(max_integer([1, 2, -3]), 2)
        self.assertEqual(max_integer([5, 10]), 10)
        self.assertEqual(max_integer([3, 5, 7]), 7)
        self.assertEqual(max_integer([-1, -2, -5]), -1)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([4]), 4)
        self.assertEqual(max_integer([3]), 3)
        self.assertEqual(max_integer([0]), 0)
        self.assertEqual(max_integer([1, 2]), 2)
        self.assertEqual(max_integer([1]), 1)
        