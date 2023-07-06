from pydantic import BaseModel, PositiveInt

class Something(BaseModel):
    a : str
    b : list[str]

m = Something(a ="do you get it ?", b =["jerlin", "do you ?"])
print (m.model_dump())