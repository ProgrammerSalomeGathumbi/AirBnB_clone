#!/usr/bin/env python3
"""
Module for BaseModel class.
"""
import uuid
from datetime import datetime


class BaseModel:
    """
    BaseModel class that defines all common attributes for other classes.
    """
    def __init__(self, *args, **kwargs):
        """
        Constructor method for BaseModel instances.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        value = (datetime.strptime
                                 (value, '%Y-%m-%dT%H:%M:%S.%f'))
                    setattr(self, key, value)
                self.id = kwargs.get('id', str(uuid.uuid4()))
                self.created_at = kwargs.get('created_at', datetime.now())
                self.updated_at = kwargs.get('updated_at', self.created_at)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """
        Returns a string representation of a BaseModel instance.
        """
        return "[{}] ({}) {}".format(type(self).__name__, self.id,
                                     self.__dict__)

    def save(self):
        """
        Updates the public instance attribute with the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all keys of __dict__ .
        """
        obj_dict = self.__dict__.copy()
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        obj_dict['__class__'] = self.__class__.__name__
        return obj_dict
