from datetime import datetime

import requests
from celery import Celery
from loguru import logger

from crud import crud_add_weather
from schemas import WeatherIn

app = Celery(
    "tasks",
    broker="redis://localhost:6379/0",
    backend="sqla+postgresql://user:password@database:5432/alpha",
)


@app.task
def task_add_weather(city: str) -> WeatherIn:
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city},uk&APPID=56358367861cbe27744e5006e5245eda"
    response = requests.get(url).json()
    logger.info(f'response:{response}')
    weather = WeatherIn(
        city=city.lower(),
        date=datetime.fromtimestamp(response["dt"]).date(),
        temp=response['main']['temp'],
    )
    crud_add_weather(weather)
    return weather
