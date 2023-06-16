#!/usr/bin/python3
"""test"""

import unittest
from max_integer import max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertEqual(max_integer([1, 2, -3]), 2)
        self.assertEqual(max_integer([5, 10]), 5)
        self.assertEqual(max_integer([3, 5, 7]), 5)
        self.assertEqual(max_integer([-1, -2, -5]), -1)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([4]), 4)

if __name__ == '__main__':
    unittest.main()
