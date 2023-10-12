#!/usr/bin/python3
"""
Shebang to make a PY script
"""

import uuid
from datetime import datetime


class BaseModel:
    """base model class define all common attributes/methods"""
    def __init__(self, *args, **kwargs):
        """raise a unique id when class mode is called"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    if key != '__class__':
                        setattr(self, key, value)

    def save(self):
        """to update instance with current datetime updated at"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """to convert into dictinory with key and value pair"""
        result = self.__dict__.copy()
        result['__class__'] = self.__class__.__name__
        result['created_at'] = self.created_at.isoformat()
        result['updated_at'] = self.updated_at.isoformat()
        return result

    def __str__(self):
        """to convert our code into strings"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
