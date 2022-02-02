import sys
import json
import sqlite3


connection = sqlite3.connect('carDb.db')

with open(sys.argv[1]) as f:
    jsonFile = json.load(f)

    cursor = connection.cursor()
    for carData in jsonFile["carDetails"]:

        try:
            cmd = f"""INSERT INTO carsData (carPlate, carModel, carManufacturer)  
                    VALUES ('{carData["carPlate"]}', '{carData["carModel"]}', '{carData["carManufacturer"]}')"""
            cursor.execute(cmd)
        except sqlite3.IntegrityError:
            pass
        finally:
            connection.commit()
    
    connection.close()
