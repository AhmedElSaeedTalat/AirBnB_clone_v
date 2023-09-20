#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models import hb_storage
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.place import place_amenity


class Amenity(BaseModel, Base):
    __tablename__ = "amenities"
    if hb_storage == "db":
        name = Column(String(128), nullable=False)
        place_amenities = relationship('Place',
                                       secondary=place_amenity,
                                       back_populates='amenities')
    else:
        name = ""
