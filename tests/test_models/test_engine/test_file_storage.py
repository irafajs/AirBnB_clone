#!/usr/bin/python3
"""
Shebang to create py script
"""


import unittest
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """test class to test FileStorage class"""
    def setUp(self):
        """Method to setup the testing"""
        self.storage = FileStorage()
        self.base_model = BaseModel()
        self.storage.new(self.base_model)
        self.storage.save()

    def tearDown(self):
        """method to remove"""
        if os.path.exists(self.storage._FileStorage__file_path):
            os.remove(self.storage._FileStorage__file_path)

    def test_all(self):
        """method to test all method"""
        objects = self.storage.all()
        self.assertIsInstance(objects, dict)
        self.assertIn("{}.{}".format(
            self.base_model.__class__.__name__, self.base_model.id), objects)

    def test_new(self):
        """method to test new method"""
        new_model = BaseModel()
        self.storage.new(new_model)
        objects = self.storage.all()
        self.assertIn(
                f"{new_model.__class__.__name__}.{new_model.id}", objects)

    def test_save(self):
        """method to test save method"""
        objects = self.storage.all()
        self.base_model.save()
        self.storage.reload()
        reloaded_objects = self.storage.all()
        self.assertEqual(objects, reloaded_objects)


if __name__ == '__main__':
    unittest.main()
