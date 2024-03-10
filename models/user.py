#!/usr/bin/python3
"""Module contains the User Class"""
from models.base_model import BaseModel


class User(BaseModel):
    """class User that inherits from BaseModel
    Attributes: email, password, firstname, last_name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
