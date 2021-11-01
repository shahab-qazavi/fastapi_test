from fastapi import FastAPI
from mongo_stuff import MongoReporter

app = FastAPI()


@app.get('/average-price')
async def avg_price():
    return MongoReporter().average_price()


@app.get('/check-price')
async def check_price():
    return None
