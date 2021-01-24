"""Home endpoints."""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import schemas, crud
from app.database import get_db

router = APIRouter()


@router.get('/home', response_model=schemas.Home)
def get_home(db: Session = Depends(get_db)):
    """Return temperature and lights."""
    return crud.homes.get_home(db=db)


@router.put('/home')
def update_home(request: schemas.ChangeTemp, db: Session = Depends(get_db)):
    """Change temperature of home."""
    return crud.homes.change_temperature(request=request, db=db)
