from fastapi import FastAPI
from pydantic import BaseModel

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
    return {
        "meter_id": reading.meter_id,
        "grid_sector": reading.grid_sector,
        "city_zone": reading.city_zone,
        "voltage": reading.voltage,
        "current": reading.current,
        "reading_time": reading.reading_time
    }