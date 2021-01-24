"""Pydantic models."""
from pydantic import BaseModel
import typing
import uuid


class Home(BaseModel):
    uuid: uuid.UUID
    temp: float
    lights: typing.List

    class Config:
        orm_mode = True


class Light(BaseModel):
    id: int
    location: str
    active: bool
    home_uuid: uuid.UUID

    class Config:
        orm_mode = True


class AddLight(BaseModel):
    """Create Light Request Schema."""
    location: str


class RemoveLight(BaseModel):
    """Remove Light Request Schema."""
    light_id: int


class SwitchLight(BaseModel):
    """Update Light Status by Id Request Schema."""
    light_id: int
    active: bool


class ChangeLocationLights(BaseModel):
    """Change Lights By Location Request Schema."""
    location: str
    active: bool


class ChangeTemp(BaseModel):
    """Change Temperature Request Schema."""
    temp: float
