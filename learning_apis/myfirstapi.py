from fastapi import FastAPI

app = FastAPI()


async def get_data():
    a = {"name":"jerlin","company_name":"e2eHiring" }
    return a

@app.post('/post/api')
async def dummy(data:dict):
        return data

# def get_data():
#     a = {"name":"Jerlin Joseph","company_name":"e2eHiring"}
#     return a

@app.get('/dummy/api')
async def return_data():
    data = get_data()
    return data