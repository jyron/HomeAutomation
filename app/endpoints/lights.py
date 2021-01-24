"""Lights endpoints."""

import typing
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import crud, schemas, models
from app.database import get_db

router = APIRouter()


@router.get('/lights')
def get_all_lights(db: Session = Depends(get_db)) -> typing.List[models.Light]:
    """Return all lights."""
    return crud.lights.get_all_lights(db=db)


@router.get('/lights/location/{location}')
def get_light_by_location(location: str, db: Session = Depends(get_db)) -> typing.List[models.Light]:
    """Return lights based on location."""
    return crud.lights.get_lights_by_location(location=location, db=db)


@router.put('/lights/location/{location}')
def update_light_by_location(request: schemas.ChangeLocationLights, db: Session = Depends(get_db)):
    """Update Lights based on location."""
    return crud.lights.update_lights_by_location(request=request, db=db)


# GOOD
@router.get('/lights/{light_id}', response_model=schemas.Light)
def get_light_by_id(light_id: int, db: Session = Depends(get_db)) -> models.Light:
    """Return a light based on id."""
    return crud.lights.get_light_by_id(light_id=light_id, db=db)


@router.post('/lights', response_model=schemas.Light)
def create_light(request: schemas.AddLight, db: Session = Depends(get_db)):
    """Add a light fixture."""
    return crud.lights.create_light(db=db, request=request)


@router.put('/lights/{light_id}', response_model=schemas.Light)
def update_light(light_id, request: schemas.SwitchLight, db: Session = Depends(get_db)):
    """Update a light status."""
    request.light_id = light_id
    return crud.lights.update_light(db=db, request=request)


@router.delete('/lights/{light_id}')
def remove_light(light_id, db: Session = Depends(get_db)):
    """Delete a light based on Id."""
    return crud.lights.remove_light(db=db, light_id=light_id)
