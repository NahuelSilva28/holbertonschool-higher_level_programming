import unittest
from unittest.mock import patch
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_area(self):
        r = Rectangle(5, 10)
        self.assertEqual(r.area(), 50)

    def test_display(self):
        r = Rectangle(3, 3)
        expected_output = "###\n" \
                          "###\n" \
                          "###\n"
        with patch('builtins.print') as mock_print:
            r.display()
            mock_print.assert_called_once_with(expected_output)

    def test_update(self):
        r = Rectangle(2, 2, 1, 1, 1)
        r.update(2, 3, 3)
        self.assertEqual(r.width, 3)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 1)
        self.assertEqual(r.id, 2)

    def test_string_representation(self):
        r = Rectangle(4, 4, 2, 3, 10)
        expected_output = "[Rectangle] (10) 2/3 - 4/4"
        self.assertEqual(str(r), expected_output)


if __name__ == '__main__':
    unittest.main()
