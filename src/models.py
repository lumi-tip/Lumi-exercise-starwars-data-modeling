import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    user_name = Column(String(250), nullable=False)
    name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)

class Planet(Base):
    __tablename__ = "planet"

    id = Column(Integer, primary_key = True)
    name = Column(String(250), nullable=False)
    population = Column(Integer, nullable=False)
    diameter = Column(Integer, nullable=False)

class Character(Base):
    __tablename__ = "character"

    id = Column(Integer, primary_key = True)
    name = Column(String(250), nullable=False)
    hair_color = Column(String(30), nullable=False)
    race = Column(String(30), nullable=False)

class FavoritePlanet(Base):
    __tablename__ = 'favorite_planet'

    id = Column(Integer, primary_key=True)
    fav_from_id = Column(Integer, ForeignKey('user.id'))
    planet_id = Column(Integer, ForeignKey('planet.id'))
    
    user = User()
    planet = Planet()

class FavoriteCharacter(Base):
    __tablename__ = 'favorite_character'

    id = Column(Integer, primary_key=True)
    fav_from_id = Column(Integer, ForeignKey('user.id'))
    character_id = Column(Integer, ForeignKey('character.id'))
    
    user = User()
    character = Character()


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
