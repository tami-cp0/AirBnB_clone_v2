#!/usr/bin/python3
""" Place Module for HBNB project """
import os
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship
from models.review import Review
from models.amenity import Amenity


# many-to-many between place and amenities
place_amenities = Table(
    'place_amenities', Base.metadata,
    Column('place_id', String(60), ForeignKey('places.id'),
       nullable=False, primary_key=True),
    Column('amenity_id', String(60), ForeignKey('amenities.id'),
       nullable=False, primary_key=True)
)

class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'

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

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship(
            'Review', backref='place', cascade='all, delete, delete-orphan'
        )
        amenities = relationship(
            'Amenity', secondary=place_amenities, backref='places', viewonly=False
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
        
        @property
        def amenities(self):
            """
            Getter for amenities that returns the list of Amenity instances
            linked to the Place through amenity_ids.
            """
            # Retrieve instances of amenity
            linked_amenities = []

            for amenity in models.storage.all(Amenity):
                if getattr(amenity, 'amenity_ids', None) == self.id:
                    linked_amenities.append(amenity)

            return self.amenities

        @amenities.setter
        def amenities(self, obj):
            """
            Setter that adds an Amenity.id to the amenity_ids list if obj is an Amenity instance.
            """
            if isinstance(obj, Amenity) and obj.id not in self.amenity_ids:
                self.amenity_ids.append(obj.id)
