import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    password = Column(String(250))
    email = Column(String(250))

class Characters(Base):
    __tablename__ = 'characters'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    heigth = Column(String(250))
    mass = Column(String(250))
    hair_color = Column(String(250))
    eye = Column(String(250))
    birth_year = Column(String(250))
    gender = Column(String(250))

class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    diameter = Column(String(250))
    rotation_period = Column(String(250))
    orbital_period = Column(String(250))
    gravity = Column(String(250))
    population = Column(String(250))
    climate = Column(String(250)) 
    terrain = Column(String(250)) 
    surface_water = Column(String(250)) 
    created = Column(String(250)) 
    edited = Column(String(250)) 
    name = Column(String(250)) 

class Ships(Base):
    __tablename__ = 'ships'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    model = Column(String(250))
    starship_class = Column(String(250))
    cost_in_credits = Column(String(250))
    lenght = Column(String(250))
    crew = Column(String(250))
    passengers = Column(String(250)) 
    max_atmosphering_speed = Column(String(250)) 
    hyperdrive_rating = Column(String(250)) 
    mGLT = Column(String(250)) 
    cargo_capcity = Column(String(250)) 
    consumables = Column(String(250))       

class Favorite_characters(Base):
    __tablename__ = 'favorite_characters'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute. 
    id = Column(Integer, primary_key=True)  
    user_id = Column(Integer, ForeignKey('users.id'))
    character_id = Column(Integer, ForeignKey('characters.id'))

class Favorite_planets(Base):
    __tablename__ = 'favorite_planets'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    planets_id = Column(Integer, ForeignKey('planets.id'))

class Favorite_ships(Base):
    __tablename__ = 'favorite_ships'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    ships_id = Column(Integer, ForeignKey('ships.id'))

    #def tos_dict(self):
        #return {}#

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')