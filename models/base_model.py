#!/usr/bin/python3
"""A class BaseModel that defines all common attributes for other classess"""
import uuid
from datetime import datetime 
import models


class BaseModel:
    """A base class for all other classes"""
    
    def __init__(self, *args, **kwargs):
        """initalize the new Base class. 
        Args:
        *args (any): Unused. 
        **kwargs (dict): key/value pairs of attributes. 
        """
        tform = "%Y-%m-%dT%H:%M:%S.%f" 
        self.id = str(uuid4()) 
        self.created_at = datetime.today()
        self.updated_at =datetime.today() 
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__ditc__[k] = datetime.strptime(v, tform)
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
        Includes the key pair __class__representign the name of the object. 
        """
        rdict = self.__self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat() 
        rdict["__class__"] = self.__class__.__name__ 
        return rdict 

    def __str__(self): 
        """Return the print/str representation of the BaseModel instance.""" 
        clname = self.__class__.__name__ 
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)
