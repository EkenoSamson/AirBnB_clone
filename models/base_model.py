#!/usr/bin/python3
""" module contains the parent class BaseModel"""
import uuid
from datetime import datetime


class BaseModel(object):
    """class that defines all common attributes/methods for other classes"""
    def __init__(self):
        """declares and initialise instance variables"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """ print: [<class name>] (<self.id>) <self.__dict__>"""
        return ("[{}] ({}) {}>".format(type(self).__name__,
            self.id, self.__dict__))

    def save(self):
        """update the current updated_at"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__ """
        dict = self.__dict__.copy()
        dict["__class__"] = type(self).__name__
        dict["created_at"] = self.created_at.isoformat()
        dict["updated_at"] = self.updated_at.isoformat()

        return dict

