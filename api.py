# import pymysql
# from dbutils.pooled_db import PooledDB
# from pydantic import BaseModel
# from fastapi import FastAPI
# from datetime import datetime, date
# from config import DB_HOST, DB_USER, DB_PASSWD, DB_NAME
# from fastapi.middleware.cors import CORSMiddleware
# import app
# app = FastAPI()
#
# pool = PooledDB(creator=pymysql,
#                 host=DB_HOST,
#                 user=DB_USER,
#                 password=DB_PASSWD,
#                 database=DB_NAME,
#                 maxconnections=1,
#                 blocking=True)
#
# class TempValue(BaseModel):
#     ts: datetime
#     temp: float
#     heatstroke: str
#
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # Replace with your allowed origins
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )
#
# def measurement_temp(temp: float) -> str:
#     if temp < 38:
#         return "low"
#     elif 38.1 <= temp <= 40.0:
#         return "moderate"
#     else:
#         return "high"
#
# @app.get("/data/temp/avg/weekly")
# async def get_temp_avg_weekly() -> list[TempValue]:
#     with pool.connection() as conn, conn.cursor() as cursor:
#         cursor.execute("""
#             SELECT DATE(ts) as date, AVG(temp) as avg_temp
#             FROM temp
#             WHERE ts >= DATE_SUB(CURDATE(), INTERVAL 7 DAY)
#             GROUP BY DATE(ts)
#             ORDER BY DATE(ts)
#         """)
#         result = [TempValue(ts=ts, temp=temp, heatstroke=measurement_temp(temp)) for ts, temp in cursor.fetchall()]
#     return result
#
# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)