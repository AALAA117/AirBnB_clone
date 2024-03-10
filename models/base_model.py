#!/usr/bin/python3
"""Basic Module for AirBnB Project"""
import uuid
from datetime import datetime
from datetime import timedelta


class BaseModel:
    """defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """initialization"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            d = {}
            form = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        setattr(self, key, datetime.strptime(value, form))
                    else:
                        setattr(self, key, value)

    def __str__(self):
        """print a specific format for instances"""
        dic_str = {
                "id": self.id,
                "created_at": self.created_at,
                "updated_at": self.updated_at,
                'my_number': 89,
                'name': 'My First Model'
                }
        name_class = self.__class__.__name__
        return ("[{}] ({}) {}".format(name_class, self.id, dic_str))

    def save(self):
        """update updated_time"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """return dictionary of all instances"""
        dict_class = self.__dict__.copy()
        dict_class["created_at"] = str(self.created_at.isoformat())
        dict_class["updated_at"] = str(self.updated_at.isoformat())
        dict_class["__class__"] = self.__class__.__name__
        return (dict_class)
