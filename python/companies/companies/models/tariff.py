import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.dialects.postgresql.json import JSON
from sqlalchemy.dialects.postgresql.array import ARRAY
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from companies.models.base import Base
from abc import ABC, abstractmethod, abstractclassmethod

class BaseTariffVal(ABC):
    @abstractmethod
    def get_type(self):
        pass

    @abstractmethod
    def get_value(self):
        pass

    @abstractmethod
    def get_compatibility(self):
        pass

    @abstractclassmethod
    def from_dict(cls, dict):
        pass

class MonoTariffVal(BaseTariffVal):
    def __init__(self, val):
        self.val = val

    def get_type(self):
        return 1

    def get_compatibility(self):
        return [1, 2, 3, 4]

    def get_value(self):
        return {
            "val": self.val
        }

    @classmethod
    def from_dict(cls, dict):
        return cls.__init__(dict["val"]) 

class Tariff(Base):
    __tablename__ = 'tariffs'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    tariff_type = Column(Integer)
    vals = Column(JSON)
    company = Column(Integer, ForeignKey('companies.id'))
    compatibility = Column(ARRAY(Integer))

    def __init__(self, name, val, company, id=None):
        if not isinstance(val, BaseTariffVal):
            raise ValueError()
        self.id = id
        self.name = name
        self.tariff_type = val.get_type()
        self.vals = val.get_value()
        self.company = company
        self.compatibility = val.get_compatibility()

    @property
    def tariff(self):
        if (self.tariff_type == 1):
            return MonoTariffVal.from_dict(self.val)
        raise ValueError()

    def __repr__(self):
        return """
            {{
                "id": {},
                "name": {},
                "tariff_type": {},
                "vals": {},
                "company": {},
                "compatibility": {}
            }}
        """.format(self.id,
                   self.name,
                   self.tariff_type,
                   self.vals,
                   self.company,
                   self.compatibility)
