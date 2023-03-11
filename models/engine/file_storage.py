#!/usr/bin/ python3
"""This is the FileStorage class."""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """This is the abstracted storage engine.
    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        ocname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(ocname, obj.id)] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        with open(FileStorage.__file_path, mode='w') as jsonFile:
            obj_dict = {}
            for key in FileStorage.__objects.keys():
                obj_dict[key] = FileStorage.__objects[key].to_dict()
            jsonFile.write(json.dumps(obj_dict))

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        if os.path.isfile(FileStorage.__file_path):
            try:
                with open(FileStorage.__file_path, mode='r') as jFile:
                    obj = json.load(jFile)
                    for key in obj.keys():
                        class_name = obj[key]["__class__"]
                        new_obj = self.selectClass(class_name)(obj[key])
                        FileStorage.__objects[key] = new_obj
            except Exception as e:
                return
