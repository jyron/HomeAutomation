"""Lights Crud functions."""
import typing
from sqlalchemy.orm import Session

from app import models, schemas, main


def get_all_lights(db: Session) -> typing.List[models.Light]:
    """Return location and status of all lights."""
    return db.query(models.Light).all()


def get_light_by_id(db: Session, light_id: int) -> models.Light:
    """Return location and status of one light."""
    return db.query(models.Light).filter(models.Light.id == light_id).first()


def get_lights_by_location(db: Session, location: str) -> typing.List[models.Light]:
    """Return all lights for a given location."""
    location = location.title()
    return db.query(models.Light).filter(models.Light.location == location).all()


def update_lights_by_location(db: Session, request:schemas.ChangeLocationLights) -> typing.List[models.Light]:
    """Update all lights for a given location."""
    location = request.location.title()
    lights = db.query(models.Light).filter(models.Light.location == location).all()
    for light in lights:
        light.active = request.active
        db.commit()
        db.refresh(light)
    return lights


def create_light(db: Session, request: schemas.AddLight) -> models.Light:
    """Add a light fixture."""
    light = models.Light(**request.dict(), home_uuid=main.MYHOMEID)
    light.location = light.location.strip().title()
    db.add(light)
    db.commit()
    db.refresh(light)
    return light


def update_light(db: Session, request: schemas.SwitchLight) -> models.Light:
    """Turn light on or off."""
    light = db.query(models.Light).filter(models.Light.id == request.light_id).first()
    if light:
        light.active = request.active
        db.commit()
        db.refresh(light)
        return light


def remove_light(db: Session, light_id:int):
    """Remove Light Fixture."""
    db.query(models.Light).filter(models.Light.id == light_id).delete()
    db.commit()
