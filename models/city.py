#!/usr/bin/python3
"""
Shebang to create PY script
"""


from models.base_model import BaseModel


class City(BaseModel):
    """method to define City fields"""
    state_id = ""
    name = ""
