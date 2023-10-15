#!/usr/bin/python3
"""
Shebang to create PY script
"""

from models.base_model import BaseModel


class User(BaseModel):
    """class user to handle user details"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
