import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class Test_Base(unittest.TestCase):
    def test_2(self):
        a = Base()
        self.assertEqual(a.id, 1)
        b = Base(5)
        self.assertEqual(b.id, 4)


    if __name__ == '__main__':
        unittest.main()