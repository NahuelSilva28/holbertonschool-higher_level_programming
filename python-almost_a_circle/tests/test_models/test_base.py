#!/usr/bin/python3
"""Unit tests for the base module"""

import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """Test cases for the Base class"""

    def test_base_id(self):
        """Test base id assignment"""
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

        b3 = Base(10)
        self.assertEqual(b3.id, 10)

if __name__ == '__main__':
    unittest.main()
