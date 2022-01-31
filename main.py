from SQLfunctions import getCarModel
from fastapi import FastAPI
from typing import Optional


app = FastAPI()


@app.get("/getCarName/byPlate/{carPlate}")
async def getCarName(carPlate: str,  q: Optional[str] = None):
    carModel = await getCarModel(carPlate)
    return {"carModel": carModel}
