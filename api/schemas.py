from datetime import date

from pydantic import BaseModel


class WeatherIn(BaseModel):
    city: str
    date: date
    temp: float


class WeatherOut(BaseModel):
    date: date
    temp: float
