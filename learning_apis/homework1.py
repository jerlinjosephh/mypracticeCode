# from fastapi import FastAPI

# app = FastAPI()

# def sum_of_integers(a,b):
#     result = a + b
#     return result

# @app.post('/pleasegive/thesum')
# async def dummy(data:dict):
#     data = sum_of_integers(2,3)
#     return data


from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Numbers(BaseModel):
    integer1: int
    integer2: int

@app.post('/add')
def add_numbers(numbers: Numbers):
    result = numbers.integer1 + numbers.integer2
    return {'result': result}