import pymysql

async def getCarModel(carPlate: str):
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='root',
                                 db='carDB')
    try:
        with connection.cursor() as cursor:
            cmd = f"""SELECT carManufacturer, carModel FROM carsData WHERE carPlate = '{carPlate}'"""
            cursor.execute(cmd)
            return cursor.fetchone()
    finally:
        connection.close()
