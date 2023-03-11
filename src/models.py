import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    userName = Column(String(250), nullable=False)
    firstName = Column(String(250), nullable=False)
    lastName = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    hairColor = Column(String(250), nullable=True)
    eyeColor = Column(String(250), nullable=True)
    skinColor = Column(String(250), nullable=True)
    height = Column(Integer, nullable = True)
    mass = Column(Integer, nullable = True)
    gender = Column(String(250), nullable = True)
    birthYear = Column(String(250), nullable = True)
    homeWorld = Column(String(250), nullable = True)
    url = Column(String(250), nullable = True)
    description = Column(String(250), nullable = True)

class UserFavorites(Base):
    __tablename__= 'user_favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    character_id = Column(Integer, ForeignKey('character.id'))
    character_planet = Column(Integer, ForeignKey('planets.id'))
    character_starship = Column(Integer, ForeignKey('starship.id'))
    residents = Column(Integer, ForeignKey('residence.id'))
    
class Planets(Base):
    __tablename__='planets'
    id = Column(Integer, primary_key=True)
    rotation_period= Column(Integer,primary_key=True)
    climate = Column(String(250), primary_key = True)
    terrain = Column(String(250), primary_key = True)
    character_id = Column(Integer, ForeignKey('character.id'))
    residents = Column(Integer, ForeignKey('residents.id'))
class StarShip(Base):
    __tablename__= 'starship'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    model = Column(String(250), primary_key = True)
    cost_in_credits = Column(Integer, primary_key = True)
    crew = Column(Integer, nullable= True)
    character_id = Column(Integer, ForeignKey('character.id'))

class Residents(Base):
    __tablename__= 'residents'
    id = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey('character.id'))
    character_planet = Column(Integer, ForeignKey('planets.id'))






#class Address(Base):
    #__tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
   # id = Column(Integer, primary_key=True)
   # street_name = Column(String(250))
    #street_number = Column(String(250))
    #post_code = Column(String(250), nullable=False)
    #person_id = Column(Integer, ForeignKey('person.id'))
    #person = relationship(Person)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')

