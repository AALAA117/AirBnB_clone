#!/usr/bin/python3
"""Basic Module for AirBnB Project"""
from .base_model import BaseModel


class User(BaseModel):
    """class User that inherits from BaseModel"""
    email = ""
    passward = ""
    first_name = ""
    last_name = ""
