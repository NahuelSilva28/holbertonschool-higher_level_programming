import unittest
from unittest.mock import patch
from io import StringIO
from models.base import Base

class TestBase(unittest.TestCase):
    def test_id_incrementation(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_id_assignment(self):
        b = Base(10)
        self.assertEqual(b.id, 10)

    def test_to_json_string(self):
        b = Base(1)
        self.assertEqual(Base.to_json_string([b.to_dictionary()]), '[{"id": 1}]')

    def test_from_json_string(self):
        b = Base.from_json_string('[{"id": 1}]')
        self.assertEqual(b[0].id, 1)

    def test_save_to_file(self):
        b1 = Base(1)
        b2 = Base(2)
        Base.save_to_file([b1, b2])
        with open("Base.json", "r") as file:
            content = file.read()
            self.assertEqual(content, '[{"id": 1}, {"id": 2}]')

    def test_load_from_file(self):
        b1 = Base(1)
        b2 = Base(2)
        Base.save_to_file([b1, b2])
        loaded_objs = Base.load_from_file()
        self.assertEqual(loaded_objs[0].id, 1)
        self.assertEqual(loaded_objs[1].id, 2)

    def test_create(self):
        b = Base.create(**{"id": 1})
        self.assertEqual(b.id, 1)

    def test_load_from_file_csv(self):
        b1 = Base(1)
        b2 = Base(2)
        Base.save_to_file_csv([b1, b2])
        loaded_objs = Base.load_from_file_csv()
        self.assertEqual(loaded_objs[0].id, 1)
        self.assertEqual(loaded_objs[1].id, 2)

    @patch('sys.stdout', new_callable=StringIO)
    def test_display(self, mock_stdout):
        b = Base(1)
        b.display()
        self.assertEqual(mock_stdout.getvalue(), '#\n')

if __name__ == "__main__":
    unittest.main()
