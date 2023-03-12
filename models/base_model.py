#!/usr/bin/python3
<<<<<<< HEAD
"""Defines the BAseModel class."""
=======
"""Defines the BaseModel for the Airbnb console"""
>>>>>>> 350e0caa10a0d522be9904841b0149ab52278d01
import models
from uuid import uuid4
from datetime import datetime
class BaseModel:
<<<<<<< HEAD
    """Represents the Base model of the HBnB project"""
    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel.

        Args:
        *args (any): unused
        **kwargs (dict): key pairs of attributes
        """

        tform = "%Y-%m-%dT%H:%M:%S.%f"
=======
    """basemodel that defines all common attributes for other classes"""
    def __init__(self, *args, **kwargs):
        """Initialize the BaseModel class
        Attributes:
        Args:
            *args (any): inputted arguments
            **kwargs (dict): Key/value pairs of inputted arguments
        id (str) - assign with an uuid when an instance is created.
        created_at (time): datetime - assign with the current datetime when
            an instance is created
        updated_at (time): datetime - assign with the current datetime when
            n instance is created and it will be updated every time you
            change your object.
        """
        timeform = "%Y-%m-%dT%H:%M:%S.%f"
>>>>>>> 350e0caa10a0d522be9904841b0149ab52278d01
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
<<<<<<< HEAD
                if k == "created at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, tform)
=======
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, timeform)
>>>>>>> 350e0caa10a0d522be9904841b0149ab52278d01
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def save(self):
<<<<<<< HEAD
        """Updated_at with the current datetime"""
=======
        """Updates the updated_at attribute with the current datetime"""
>>>>>>> 350e0caa10a0d522be9904841b0149ab52278d01
        self.updated_at = datetime.today()
        models.storage.save()
    def to_dict(self):
<<<<<<< HEAD
        """Return the dictionary of the BAseModel instance


        Includes the key value pair __class__ representing
        the classs name of the object.
        """
        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["__class__"] = self.__class__.__name__
        return rdict

    def __str__(self):
        """Return the print representation of the BaseModel instance"""
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)
=======
        """Return the dictionary of the __dict__ of the instance.
        Return:
            dictonary (dict): Dictionary object that contains __dict__
        """
        returndict = self.__dict__.copy()
        returndict["created_at"] = self.created_at.isoformat()
        returndict["updated_at"] = self.updated_at.isoformat()
        returndict["__class__"] = self.__class__.__name__
        return returndict
    def __str__(self):
        """str representation of the BaseModel class
        Return:
            string(str): string descriptor for the BaseModel Class
        """
        classname = self.__class__.__name__
        return "[{}] ({}) {}".format(classname, self.id, self.__dict__)
>>>>>>> 350e0caa10a0d522be9904841b0149ab52278d01
