from fastapi import FastAPI,HTTPException,Request
from to_db import insertdata
from schema import userschema
from schema import userlogin
from db import engine

from to_db import checklogin

app=FastAPI()
@app.post('/createuser')
async def createUser(request:Request,data:userschema=None):
    if data is None or data==None:
        raise HTTPException(status_code=205,detail="Please Enter a valid feild")   
    request_data = await request.json()
    field_schema=userschema.__annotations__
    unknown_field=[x for x in request_data if x not in field_schema]
    if len(unknown_field) >0:
        ouptut= {"message":"Please Enter a valid Field",
            "ie":f"{[x for x in field_schema]}",
            "unkown_field":f"{unknown_field}" }
        raise HTTPException(status_code=400,detail=ouptut)   
    return insertdata(data)

@app.post('/login')
def loginuser(user:userlogin):
    return checklogin(user)
    

if __name__=="__main__":
    import uvicorn
    uvicorn.run(app="main:app",host="localhost",reload=True)