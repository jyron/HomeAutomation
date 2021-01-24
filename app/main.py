"""App entrypoint."""
from fastapi import FastAPI
from . import models, endpoints
from .database import engine, SessionLocal
import uuid
app = FastAPI()
app.include_router(endpoints.lights.router)
app.include_router(endpoints.homes.router)

MYHOMEID = uuid.uuid4()


@app.on_event("startup")
async def startup_event():
    """Sample values for Db, Not intended for production."""
    print('Initializing DB...\n')
    models.Base.metadata.drop_all(bind=engine)
    models.Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    initial_values = [models.Home(uuid=MYHOMEID, temp=73),
                      models.Light(home_uuid=MYHOMEID, location='Bedroom', active=True),
                      models.Light(home_uuid=MYHOMEID, location='Kitchen', active=False)
                      ]
    for val in initial_values:
        db.add(val)
        db.commit()

    home = db.query(models.Home).first()
    print(f'MYHOMEID: {home.uuid}')
    print(f'Home Temp: {home.temp} Degrees.')
    print(f'No. of Lights: {len(home.lights)} lights.\n')
    for light in home.lights:
        print("Light Id:", light.id)
        print("Location:", light.location)
        print("Active:", light.active, '\n')
    db.close()
