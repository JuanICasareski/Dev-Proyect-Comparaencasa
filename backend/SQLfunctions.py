from functools import lru_cache
import sqlite3
import time

@lru_cache(maxsize=100)  
def getCarModel(carPlate: str):
    connection = sqlite3.connect('carDb.db')

    try:
        cursor = connection.cursor()
        cmd = f"""SELECT carManufacturer, carModel FROM carsData WHERE carPlate = '{carPlate}'"""
        cursor.execute(cmd)
        return cursor.fetchone()
    finally:
        connection.close()
