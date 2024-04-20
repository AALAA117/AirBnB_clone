#!/usr/bin/python3
"""File Storage"""
import json
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """store data"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary"""
        return (FileStorage.__objects)

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        dic_to_json = {}
        for key, obj in FileStorage.__objects.items():
            dic_to_json[key] = obj.to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(dic_to_json, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, "r") as content:
                data = json.load(content)
            for key, value in data.items():
                FileStorage.__objects[key] = eval(value['__class__'])(**value)
        except Exception as err:
            pass
