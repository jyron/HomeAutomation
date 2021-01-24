"""Home Crud functions."""
from sqlalchemy.orm import Session
from app import models, main, schemas


def get_home(db: Session) -> models.Home:
    """Return temperature and lights info for a home."""
    return db.query(models.Home).filter(models.Home.uuid == main.MYHOMEID).first()


def change_temperature(db: Session, request: schemas.ChangeTemp) -> models.Home:
    home = db.query(models.Home).filter(models.Home.uuid == main.MYHOMEID).first()
    home.temp = request.temp
    return home
