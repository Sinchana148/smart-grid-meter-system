from fastapi import FastAPI
from pydantic import BaseModel
from app.db import conn, cursor

app = FastAPI()

class MeterReading(BaseModel):
    meter_id: str
    grid_sector: str
    city_zone: str
    voltage: float
    current: float
    reading_time: str

@app.get("/")
def home():
    return {"message": "Smart Grid API Running"}

@app.post("/meter-data")
def add_meter_data(reading: MeterReading):

    cursor.execute(
        """
        INSERT INTO meter_readings
        (meter_id, grid_sector, city_zone, voltage, current, reading_time)
        VALUES (%s, %s, %s, %s, %s, %s)
        """,
        (
            reading.meter_id,
            reading.grid_sector,
            reading.city_zone,
            reading.voltage,
            reading.current,
            reading.reading_time
        )
    )

    conn.commit()

    return {"message": "Data inserted successfully"}