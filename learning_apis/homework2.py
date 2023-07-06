# 2.Create an GET API which returns these following:
# Candidate name
# Candidate register number
# Candidate course
# Candidate mobile number
# Candidate address


from fastapi import FastAPI

app = FastAPI()
async def get_candidate_data():
    a = {'name': 'Jerlin', 'register_no': 44555, 'course': 'python', 'mobile_no' :7788655, 'address' : 'hyderabad'}
    return a 

@app.get('/myfile/api')
async def return_data():
    data= get_candidate_data()
    return data

