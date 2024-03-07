#!/usr/bin/python3
""" module contains the parent class BaseModel"""
import uuid
from datetime import datetime


class BaseModel(object):
    """class that defines all common attributes/methods for other classes"""
    def __init__(self):
        """declares and initialise instance variables"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now
        self.updated_at = datetime.now


