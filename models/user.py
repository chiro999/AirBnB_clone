#!/usr/bin/python3
""" class User Module"""
from models.base_model import BaseModel

class User(BaseModel):
    """Class for User instances that inherits BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
