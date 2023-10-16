#!/usr/bin/python3
"""
Shebang to create PY script
"""


import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """class to test BaseModel"""
    def setUp(self):
        """method setup"""
        self.base_model = BaseModel()

    def test_init(self):
        """method to test __init"""
        self.assertIsInstance(self.base_model, BaseModel)
        self.assertTrue(hasattr(self.base_model, 'id'))
        self.assertTrue(hasattr(self.base_model, 'created_at'))
        self.assertTrue(hasattr(self.base_model, 'updated_at'))
        self.assertIsInstance(self.base_model.created_at, datetime)
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_save(self):
        """method to test save method"""
        updated_at_before = self.base_model.updated_at
        self.base_model.save()
        updated_at_after = self.base_model.updated_at
        self.assertNotEqual(updated_at_before, updated_at_after)

    def test_to_dict(self):
        """method to test to_dict method"""
        base_model_dict = self.base_model.to_dict()
        self.assertIsInstance(base_model_dict, dict)
        self.assertEqual(base_model_dict['__class__'], 'BaseModel')
        self.assertEqual(base_model_dict['id'], self.base_model.id)

    def test_str(self):
        """method to test str represantation"""
        expected_str = (f"[{self.base_model.__class__.__name__}] "
                        f"({self.base_model.id}) {self.base_model.__dict__}")
        self.assertEqual(str(self.base_model), expected_str)


if __name__ == '__main__':
    unittest.main()
