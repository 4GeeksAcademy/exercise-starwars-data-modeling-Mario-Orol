import os
import sys
from sqlalchemy.orm import declarative_base, Mapped, mapped_column, relationship
from sqlalchemy import create_engine, String, ForeignKey
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    user_id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True, nullable=False)
    email: Mapped[str] = mapped_column(unique=True, nullable=False)

    favorites = relationship("Favorite", back_populates="user")
    

class Character(Base):
    __tablename__ = 'character'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    character_id: Mapped[int] = mapped_column(primary_key=True)
    character_name: Mapped[str] = mapped_column(unique=True, nullable=False)
    height: Mapped[int] = mapped_column(nullable=True)
    mass: Mapped[int] = mapped_column(nullable=True)
    hair_color: Mapped[str] = mapped_column(nullable=True)
    skin_color: Mapped[str] = mapped_column(nullable=True)
    eye_color: Mapped[str] = mapped_column(nullable=True)
    birth_year: Mapped[int] = mapped_column(nullable=True)
    gender: Mapped[str] = mapped_column(nullable=True)

    favorites = relationship("Favorite", back_populates="character")

class Planet(Base):
    __tablename__ = 'planet'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    planet_id: Mapped[int] = mapped_column(primary_key=True)
    planet_name: Mapped[str] = mapped_column(unique=True, nullable=False)
    climate: Mapped[str] = mapped_column(nullable=True)
    terrain: Mapped[int] = mapped_column(nullable=True)
    population: Mapped[int] = mapped_column(nullable=True)
    gravity: Mapped[int] = mapped_column(nullable=True)
    diameter: Mapped[int] = mapped_column(nullable=True)
    rotation_period: Mapped[int] = mapped_column(nullable=True)
    orbital_period: Mapped[int] = mapped_column(nullable=True)

    favorites = relationship("Favorite", back_populates="planet")


class Favorite(Base):
    __tablename__ = 'favorite'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    favorite_id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.user_id"))
    character_id: Mapped[int] = mapped_column(ForeignKey("character.character_id"))
    planet_id: Mapped[int] = mapped_column(ForeignKey("planet.planet_id"))
    

    user = relationship("User", back_populates="favorites")
    character = relationship("Character", back_populates="favorites")
    planet = relationship("Planet", back_populates="favorites")



# Relationships Between Tables
# One-to-Many: A User can have multiple Favorites, but a Favorite belongs to only one User.
# Many-to-One: A Favorite can be either a Character or a Planet (not both).
# One-to-Many: Each Character and Planet can be favorited by multiple users.

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
