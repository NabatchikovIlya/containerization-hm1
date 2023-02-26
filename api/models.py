from database import Base
from sqlalchemy import Column, Float, Integer, Date, String


class Weather(Base):
    __tablename__ = "Weather"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    city = Column("city", String, index=True)
    date = Column("date", Date)
    temp = Column("temp", Float)
