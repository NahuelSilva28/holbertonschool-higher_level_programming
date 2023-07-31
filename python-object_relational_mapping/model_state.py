#!/usr/bin/python3
"""This module defines the State class"""
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

# Create a new instance of the Base class
Base = declarative_base()


class State(Base):
    """This class represents the states table in the database"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

