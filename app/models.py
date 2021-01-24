"""Database Models."""
from sqlalchemy import Column, String, Integer, Boolean, ForeignKey, Float
from sqlalchemy.orm import relationship
from fastapi_utils.guid_type import GUID
from .database import Base


class Home(Base):
    __tablename__ = "homes"
    id = Column(Integer, primary_key=True, index=True)
    uuid = Column(GUID(), unique=True, index=True)
    temp = Column(Float)
    lights = relationship("Light", back_populates="house")


class Light(Base):
    __tablename__ = "lights"

    id = Column(Integer, primary_key=True, index=True)
    location = Column(String, index=True)
    active = Column(Boolean, default=False)
    home_uuid = Column(GUID, ForeignKey("homes.uuid"))
    house = relationship("Home", back_populates="lights")
