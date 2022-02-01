import sqlite3

async def getCarModel(carPlate: str):
    connection = sqlite3.connect('carDb.db')
    
    try:
        with connection.cursor() as cursor:
            cmd = f"""SELECT carManufacturer, carModel FROM carsData WHERE carPlate = '{carPlate}'"""
            cursor.execute(cmd)
            return cursor.fetchone()
    finally:
        connection.close()