import uvicorn
from fastapi import FastAPI

from pydantic import BaseModel

app = FastAPI()

class Car(BaseModel):
    name : str
    price : int
cars = [
  {"name": "Tesla", "price": 180000},
  {"name": "BMW", "price": 260000}
]


@app.get('/')
def index():
    return {'hello':'fastapi'}

@app.get('/cars')
def get_cars():
    return cars

@app.get('/cars/{id}')
def get_car(id:int):
    return  cars[id-1]

@app.post('/cars')
def create_car(car:Car):
    cars.append(car.dict())
    return cars[-1]

@app.put('/cars/{id}')
def update_car(id:int,car:Car):
    cars[id-1] = car
    return cars[id-1]

@app.delete('/cars/{id}')
def delete_car(id:int):
    cars.pop(id-1)
    return {}


if __name__ == '__main__':
    uvicorn.run('main:app',host='127.0.0.1',port=8000,
                reload=True,access_log=False)