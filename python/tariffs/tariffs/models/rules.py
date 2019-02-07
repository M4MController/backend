import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.dialects.postgresql.json import JSON
from sqlalchemy.dialects.postgresql.array import ARRAY
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from companies.models.base import Base
from abc import ABC, abstractmethod, abstractclassmethod


class Rule(Base):
    __tablename__ = 'rules'

    id = Column(Integer, primary_key=True)
    statistic = Column(Integer, nullable=False)
    sensor = Column(Integer, nullable=False)
    tags = Column(ARRAY(Integer))

    def __repr__(self):
        return """
            {{
                "id": {},
                "statistic": {},
                "sensor": {},
                "tags": {},
            }}
        """.format(self.id,
                   self.statistic,
                   self.sensor,
                   self.tags)
