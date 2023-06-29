import unittest
from base import Base


class TestBase(unittest.TestCase):
    def test_2(self):
        a = Base()
        self.assertEqual(a.id, 1)
        b = Base(5)
        self.assertEqual(b.id, 5)


if __name__ == '__main__':
    unittest.main()
