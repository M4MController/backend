import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.dialects.postgresql.json import JSON
from sqlalchemy.dialects.postgresql.array import ARRAY
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from companies.models.base import Base
from abc import ABC, abstractmethod, abstractclassmethod


class Tag(Base):
    __tablename__ = 'tags'

    id = Column(Integer, primary_key=True)
    name = Column(Integer, unique=True, nullable=False)

    def __repr__(self):
        return """
            {{
                "id": {},
                "name": {}
            }}
        """.format(self.id,
                   self.name)
