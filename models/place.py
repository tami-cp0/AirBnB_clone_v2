#!/usr/bin/python3
""" Place Module for HBNB project """
import os
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship
from models.review import Review


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship(
            'Review', backref='place', cascade='all, delete, delete-orphan'
        )
    else:
        @property
        def reviews(self):
            """
            returns the list of Review instances with place_id
            equals to the current Place.id
            """
            # Retrievs review instances
            instances = models.storage.all(Review)
            review_list = []

            for review in instances:
                if getattr(review, 'place_id', None) == self.id:
                    review_list.append(review)
            return review_list

    city_id = Column(
        String(60),
        ForeignKey('cities.id'),
        nullable=False
    )
    user_id = Column(
        String(60),
        ForeignKey('users.id'),
        nullable=False
    )
    name = Column(
        String(128),
        nullable=False
    )
    description = Column(
        String(1024)
    )
    number_rooms = Column(
        Integer,
        nullable=False,
        default=0
    )
    number_bathrooms = Column(
        Integer,
        nullable=False,
        default=0
    )
    max_guest = Column(
        Integer,
        nullable=False,
        default=0
    )
    price_by_night = Column(
        Integer,
        nullable=False,
        default=0
    )
    latitude = Column(Float)
    longitude = Column(Float)

    amenity_ids = []
