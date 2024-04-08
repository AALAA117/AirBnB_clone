"""Test Base Model"""
import unittest
import uuid
from models.base_model import BaseModel
from datetime import datetime
from datetime import timedelta


class TestBase(unittest.TestCase):
    """Test BaseModel"""
    def setUp(self):
        self.obj = BaseModel()
        self.creation_time = self.obj.created_at
        self.updated_time = self.obj.updated_at

    def test_id(self):
        """test id"""
        obj1 = BaseModel()
        self.assertEqual(self.obj.id, self.obj.id)
        self.assertNotEqual(obj1.id, self.obj.id)
        self.assertIsInstance(self.obj.id, str)
        self.assertIsInstance(uuid.UUID(self.obj.id), uuid.UUID)
        self.assertIsNotNone(self.obj.id)

    def test_created_at(self):
        """test urrent datetime when an instance is created"""
        self.assertEqual(self.obj.created_at.year, self.creation_time.year)
        self.assertEqual(self.obj.created_at.month, self.creation_time.month)
        self.assertEqual(self.obj.created_at.day, self.creation_time.day)
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_updated_at(self):
        """
        test current datetime when an instance
        is created and it will be updated
        """
        self.assertEqual(self.obj.updated_at.year, self.updated_time.year)
        self.assertEqual(self.obj.updated_at.month, self.updated_time.month)
        self.assertEqual(self.obj.updated_at.day, self.updated_time.day)
        self.assertNotEqual(self.obj.created_at, self.obj.updated_at)
        self.assertIsInstance(self.obj.updated_at, datetime)

    def test_str(self):
        """test string representation"""
        dic_str = {
                "id": self.obj.id,
                "created_at": self.obj.created_at,
                "updated_at": self.obj.updated_at,
                'my_number': 89,
                'name': 'My First Model'
                }
        expected_str = "[{}] ({}) {}".format(type(self.obj).__name__,
                                             self.obj.id, dic_str)
        self.assertEqual(str(self.obj), expected_str)

    def test_save(self):
        """test save that updates the public instance attribute updated_at"""
        self.assertEqual(self.obj.updated_at.year, self.updated_time.year)
        self.assertEqual(self.obj.updated_at.month, self.updated_time.month)
        self.assertEqual(self.obj.updated_at.day, self.updated_time.day)
        self.assertIsInstance(self.obj.updated_at, datetime)
        self.obj.save()
        updated_date = self.obj.updated_at
        self.assertNotEqual(self.updated_time, updated_date)
        self.assertIsInstance(updated_date, datetime)

    def test_to_dict(self):
        """
        test dictionary representation
        with “simple object type” of our BaseModel
        """
        a_dict = self.obj.to_dict()
        self.assertIsInstance(a_dict, dict)
        self.assertIsNotNone(a_dict)
        self.assertIsInstance(a_dict["created_at"], str)
        self.assertIsInstance(a_dict["updated_at"], str)
        self.assertEqual(a_dict["created_at"],
                         str(self.creation_time.isoformat()))
        self.assertEqual(a_dict["updated_at"],
                         str(self.updated_time.isoformat()))


if __name__ == '__main__':
    unittest.main()
