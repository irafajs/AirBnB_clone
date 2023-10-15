#!/usr/bin/python3
"""
Shebang to create a PY script
"""


import json


class FileStorage:
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Return the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Set obj in __objects with key <obj class name>.id"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Serialize __objects to the JSON file"""
        with open(FileStorage.__file_path, 'w') as f:
            serialized = {}
            for key, value in FileStorage.__objects.items():
                serialized[key] = value.to_dict()
            json.dump(serialized, f)

    def reload(self):
        """Deserialize the JSON file to __objects"""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        class_list = {
                'BaseModel': BaseModel, 'User': User, 'State': State,
                'City': City, 'Amenity': Amenity, 'Place': Place,
                'Review': Review
                }
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                serialized = json.load(f)
            for key, value in serialized.items():
                class_name, obj_id = key.split('.')
                if class_name in class_list:
                    self.__objects[key] = class_list[class_name](**value)
        except Exception:
            pass
