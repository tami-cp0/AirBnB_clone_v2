#!/usr/bin/python3
"""This module defines a class User"""


from models.base_model import BaseModel, Base
from models.place import Place
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
<<<<<<< HEAD
    __tablename__ = 'users'
    places = relationship(
        "Place", backref="user",
        cascade="all, delete, delete-orphan"
    )
=======
    __tablename__ = "users"
>>>>>>> parent of f2bf6e1 (changed table records)

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
