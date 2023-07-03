from fastapi import FastAPI

app = FastAPI()

def sum_of_integers(a,b):
    result = a + b
    return result

@app.post('/pleasegive/thesum')
async def dummy(data:dict):
    data = sum_of_integers(2,3)
    return data


# from fastapi import FastAPI, Body

# # Create an app instance
# app = FastAPI()

# # Define a route for the POST method
# @app.post('/sum')
# def sum(a: int = Body(...), b: int = Body(...)):
#     # Calculate the sum
#     result = a + b
#     # Return the sum as JSON response
#     return {'sum': result}
