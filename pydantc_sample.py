from pydantic import BaseModel, ValidationError

class Person(BaseModel):
    age: int
    name: str
    is_married: bool 
    
data = {
    # 'name':"John",
    'age': 29,
    'is_married': "False",
    "woool":"yes"
}
try:
    person = Person(**data)
    print (person.__dict__)
except ValidationError as e:
    print (e.errors())
    print ("yo")

# import pdb; pdb.set_trace()