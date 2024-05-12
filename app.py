import pymysql
from dbutils.pooled_db import PooledDB
from config import DB_HOST, DB_USER, DB_PASSWD, DB_NAME
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException
from datetime import datetime

pool = PooledDB(creator=pymysql,
                host=DB_HOST,
                user=DB_USER,
                password=DB_PASSWD,
                database=DB_NAME,
                maxconnections=1,
                blocking=True)
app = FastAPI()


# if temp less than 38 then heatstroke is "low"
# if temp is 38.1 to 40.0 then heatstroke is "moderate"
# if temp is more than 40 then heatstroke is "high"

# if pm25 less than 50 then AQIrisklevel is "low"
# if pm25 is 50.1 to 100 then AQIrisklevel is "moderate"
# if pm25 is 100.1 to 150 then AQIrisklevel is "Unhealthy for Sensitive Groups"
# if pm25 is 150.1 to 200 then AQIrisklevel is "Unhealthy"
# if pm25 is 200.1 to 300 then AQIrisklevel is "Very Unhealthy"
# if pm25 is more than 300 then AQIrisklevel is "Hazardous"

class TempValue(BaseModel):
    ts: datetime
    temp: float
    heatstroke: str


class AQIValue(BaseModel):
    ts: datetime
    pm25: float
    AQIrisklevel: str


def measurement_temp(temp: float):
    if temp < 38:
        return "low"
    elif 38.1 <= temp <= 40.0:
        return "moderate"
    else:
        return "high"


def measurement_pm25(pm25: float):
    if pm25 < 50:
        return "low"
    elif 50.1 <= pm25 <= 100:
        return "moderate"
    elif 100.1 <= pm25 <= 150:
        return "Unhealthy for Sensitive Groups"
    elif 150.1 <= pm25 <= 200:
        return "Unhealthy"
    elif 200.1 <= pm25 <= 300:
        return "Very Unhealthy"
    else:
        return "Hazardous"


@app.get("/api/temp")
async def get_temp() -> list[TempValue]:
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute("""
            SELECT ts, temp FROM temp
        """)
        result = [TempValue(ts=ts, temp=temp,
                            heatstroke=measurement_temp(temp)) for ts, temp in cs.fetchall()]
    return result


@app.get("/api/pm25")
async def get_pm25() -> list[AQIValue]:
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute("""
            SELECT ts, pm25 FROM pm25
        """)
        result = [AQIValue(ts=ts, pm25=pm25,
                           AQIrisklevel=measurement_pm25(pm25)) for ts, pm25 in cs.fetchall()]
    return result
