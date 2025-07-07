from pydantic import BaseModel

class Create_User(BaseModel):
    name: str = ""
    age: int 
    mobile_number: str = ""
    address: str = ""
