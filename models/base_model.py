#!/usr/bin/python3
import models
from datetime import datetime
from uuid import uuid4


class BaseModel:
    """BaseModel.
    """

    def __init__(self, *args, **kwargs):
        """__init__.

        Args:
            args:
            kwargs:
        """
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs != {}:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__.update({k: datetime.strptime(v, t_format)})
                elif k != "__class__":
                    self.__dict__.update({k: v})
        else:
            models.storage.new(self)

    def __str__(self):
        """__str__.
        """
        return (f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}')

    def save(self):
        """save.
        """
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """to_dict.
        """
        new_dic = self.__dict__.copy()
        new_dic['__class__'] = self.__class__.__name__
        new_dic.update({'created_at': self.created_at.isoformat()})
        new_dic.update({'updated_at': self.updated_at.isoformat()})
        return new_dic
