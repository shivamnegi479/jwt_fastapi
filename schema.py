from pydantic import BaseModel


class userschema(BaseModel):
    name:str|None
    email:str|None
    password:str|None