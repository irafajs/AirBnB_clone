#!/usr/bin/python3
"""
Shebang to create PY script
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """method to define Review"""
    place_id = ""
    user_id = ""
    text = ""
