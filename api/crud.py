from database import db_context
from models import Weather
from schemas import WeatherIn, WeatherOut


def crud_add_weather(weather: WeatherIn):
    db_weather = Weather(**weather.dict())
    with db_context() as db:
        exist = (
            db.query(Weather)
            .filter(Weather.city == weather.city, Weather.date == weather.date)
            .first()
        )
        if exist:
            return None
        db.add(db_weather)
        db.commit()
        db.refresh(db_weather)
    return db_weather


def crud_get_weather(city: str, num_rows: int = 10):
    with db_context() as db:
        weather = (
            db.query(Weather)
            .filter(Weather.city == city)
            .order_by(Weather.date.desc())
            .limit(num_rows)
            .all()
        )
    if weather:
        result = []
        for item in weather:
            result.append(WeatherOut(**item.__dict__))
        return {city: result[::-1]}
    return None


def crud_error_message(message):
    return {"error": message}
