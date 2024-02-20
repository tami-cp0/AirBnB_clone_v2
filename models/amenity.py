#!/usr/bin/python3
""" Amenity Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float


class Amenity(BaseModel, Base):
    """Amenity class"""
    __tablename__ = 'amenities'

    name = Column(
        String(60),
        nullable=False
    )
