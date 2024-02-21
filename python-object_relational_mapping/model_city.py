#!/usr/bin/python3
"""
Contains the class definition of a City.
"""
from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class City(Base):
    """
    Start of class City instance
    """
    __tablename__ = 'cities'

    id = Column(
            Integer,
            autoincrement=True,
            unique=True,
            nullable=False,
            primary_key=True
            )

    name = Column(
            String(128),
            nullable=False,
            )

    states_id = Column(
            Integer,
            ForeignKey("states.id")
            nullable=False,
            )
