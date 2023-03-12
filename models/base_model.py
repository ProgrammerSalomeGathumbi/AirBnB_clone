#!/usr/bin/python3
<<<<<<< HEAD
"""Defines the BaseModel class."""
import models
=======
"""
Module for BaseModel class.
"""
>>>>>>> 0775ecbfe8717c4595dd5983b549c2c4402acc0b
from uuid import uuid4
from datetime import datetime


class BaseModel:
<<<<<<< HEAD
    """Represents the BaseModel of the HBnB project."""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel.
        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, tform)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def save(self):
        """Update updated_at with the current datetime."""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Return the dictionary of the BaseModel instance.
        Includes the key/value pair __class__ representing
        the class name of the object.
        """
        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["__class__"] = self.__class__.__name__
        return rdict

    def __str__(self):
        """Return the print/str representation of the BaseModel instance."""
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)
=======
    """
    This is the  BaseModel class
    """

    def __init__(self, *args, **kwargs):
        """
        This is the Constructor method
        """
        from models import storage
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            self.save()
            storage.new(self)
        else:
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            del kwargs['__class__']
            self.__dict__.update(kwargs)

    def save(self):
        """
        Updates the basemodel instance with current datetime
        """
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def __str__(self):
        """
        String reprsentation for the user
        """
        return '[{}] ({}) {}'.format(
            type(self).__name__, self.id, self.__dict__)

    def to_dict(self):
        """
        Dictionary containing all
        keys/values of __dict__ of instance
        """
        my_dict = dict(self.__dict__)
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        my_dict['__class__'] = type(self).__name__
        return my_dict
>>>>>>> 0775ecbfe8717c4595dd5983b549c2c4402acc0b
