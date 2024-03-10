#!/usr/bin/python3
"""Module contains class Reviews"""
from models.base_model import BaseModel


class Reviews(BaseModel):
    """
    Inherits from BaseModel
    Attributes: place_id, user_id, text
    """
    place_id = ""
    user_id = ""
    test = ""
