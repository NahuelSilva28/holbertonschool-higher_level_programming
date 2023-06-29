import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    def test_id(self):
        # Test initialization with specific id
        b1 = Base(1)
        self.assertEqual(b1.id, 1)

        # Test automatic id assignment
        b2 = Base()
        self.assertEqual(b2.id, 2)

   
if __name__ == '__main__':
    unittest.main()
