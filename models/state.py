#!/usr/bin/python3
""" State Module for HBNB project """
import models
import os
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    cities = relationship(
        "City", backref="state",
        cascade="all, delete, delete-orphan"
    )

    name = Column(
        String(128),
        nullable=False
    )

    @property
    def cities(self):
        """
        returns the list of City instances with state_id
        equals to the current State.id
        """
        if os.getenv('HBNB_TYPE_STORAGE') == 'fs':
            # Retrievs city instances
            instances = models.storage.all(City)
            city_list = []

            for city in instances.values():
                if getattr(city, 'state_id', None) == self.id:
                    city_list.append(city)
            return city_list
