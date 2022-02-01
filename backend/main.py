from fastapi.middleware.cors import CORSMiddleware
from SQLfunctions import getCarModel
from fastapi import FastAPI
from typing import Optional


app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/getCarName/byPlate/{carPlate}")
async def getCarName(carPlate: str,  q: Optional[str] = None):
    query = await getCarModel(carPlate)
    if query is not None:
        return {"carManufacturer": query[0], "carModel": query[1]}
    return query