#!/usr/bin/env python3
"""
Module for BaseModel class.
"""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    BaseModel class that defines all common attributes for other classes.
    """
    def __init__(self, *args, **kwargs):
        """
        Constructor method for BaseModel instances.
        """
        i = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for arg, val in kwargs.items():
                if arg == 'created_at'or val == 'updated_at':
                    self.__dict__[arg] = datetime.strptime(val, i)
                else:
                    self.__dict__[arg] = val
        else:
            models.storage.new(self)

    def __str__(self):
        """
        Returns a string representation of a BaseModel instance.
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """
        Updates the public instance attribute with the current datetime.
        """
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys of __dict__ .
        """
        obj_dict = self.__dict__.copy()
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        obj_dict["__class__"] = self.__class__.__name__
        return obj_dict
