import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.dialects.postgresql.json import JSON
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from companies.models.base import Base
from abc import ABC, abstractmethod

class BaseTariffVal(ABC):
    @abstractmethod
    def get_type(self):
        pass

    @abstractmethod
    def get_value(self):
        pass

class MonoTariffVal(BaseTariffVal):
    def __init__(self, val):
        self.val = val

    def get_type(self):
        return 1

    def get_value(self):
        return {
            "val": self.val
        }

class Tariff(Base):
    __tablename__ = 'tariff'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    tariff_type = Column(Integer)
    vals = Column(JSON)
    company = Column(Integer, ForeignKey('companies.id'))

    def __init__(self, name, val, company, id=None):
        if not isinstance(val, BaseTariffVal):
            raise ValueError()
        self.id = id
        self.name = name
        self.tariff_type = val.get_type()
        self.vals = val.get_value()
        self.company = company

    @property
    def tariff(self):
        if (self.tariff_type == 1):
            return MonoTariffVal(self.val)
        raise ValueError()

    def __repr__(self):
        return """
            {{
                "id": {},
                "name": {},
                "tariff_type": {},
                "vals": {},
                "company": {}
            }}
        """.format( self.id,
                    self.name,
                    self.tariff_type,
                    self.vals,
                    self.company)
