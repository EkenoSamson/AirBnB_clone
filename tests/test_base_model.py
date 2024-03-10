#!/usr/bin/python3
"""Module contains test cases for BaseModel"""
import unittest
from  datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """testcases"""

    def test_init(self):
        t = BaseModel()
        t_2 = BaseModel()
        self.assertIsInstance(t, BaseModel)
        self.assertIsInstance(t.id, str)
        self.assertIsNot(t.id, t_2.id)
        
        """test created_at and updated_at"""
        self.assertIsInstance(t.created_at, datetime)
        self.assertIsInstance(t.updated_at, datetime)

    def test_str(self):
        t = BaseModel()
        s = ("[{}] ({}) {}>".format(type(t).__name__,
            t.id, t.__dict__))
        self.assertEqual(str(t), s)

    def test_save(self):
        t = BaseModel()
        self.assertTrue(datetime.now(), t.save())


if "__name__" == "__main__":
    unittest.main()
