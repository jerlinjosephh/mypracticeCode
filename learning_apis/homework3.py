from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Numbers (BaseModel):
    integer1 : float
    integer2 : float
    integer3 : float

@app.post('/multiply')
def mul_numbers(numbers : Numbers):
    result = numbers.integer1 * numbers.integer2 * numbers.integer3
    return {'result': result}

