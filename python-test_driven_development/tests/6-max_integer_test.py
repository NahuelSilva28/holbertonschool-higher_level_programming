import unittest
from max_integer import max_integer

class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        result = max_integer([])
        self.assertIsNone(result)

    def test_positive_numbers(self):
        result = max_integer([1, 2, 3, 4])
        self.assertEqual(result, 4)

    def test_negative_numbers(self):
        result = max_integer([-1, -2, -3, -4])
        self.assertEqual(result, -1)

    def test_single_element(self):
        result = max_integer([5])
        self.assertEqual(result, 5)

    def test_duplicate_numbers(self):
        result = max_integer([1, 1, 1, 1])
        self.assertEqual(result, 1)

    def test_mixed_numbers(self):
        result = max_integer([1, -2, 3, -4])
        self.assertEqual(result, 3)

    
if __name__ == '__main__':
    unittest.main()
