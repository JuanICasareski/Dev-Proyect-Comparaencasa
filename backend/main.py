from SQLfunctions import getCarModel
from fastapi import FastAPI
from typing import Optional


app = FastAPI()


@app.get("/getCarName/byPlate/{carPlate}")
async def getCarName(carPlate: str,  q: Optional[str] = None):
    query = await getCarModel(carPlate)
    if query is not None:
        return {"carManufacturer": query[0], "carModel": query[1]}
    return query