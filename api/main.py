from celery.result import AsyncResult

from schemas import WeatherIn
from crud import crud_error_message, crud_get_weather
from database import engine
from fastapi import FastAPI, HTTPException
from models import Base
from tasks import task_add_weather

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.post("/weathers/{city}", status_code=201)
def add_weather(city: str) -> WeatherIn:
    """
    Get weather data from api.collectapi.com/weather
    and add database using Celery. Uses Redis as Broker
    and Postgres as Backend.
    """
    task = task_add_weather(city)
    return task


@app.get("/weathers/{city}")
def get_weather(city: str):
    """
    Get weather from database.
    """
    weather = crud_get_weather(city.lower())
    if weather:
        return weather
    else:
        raise HTTPException(
            404, crud_error_message(f"No weather found for city: {city}")
        )
