from fastapi import FastAPI,HTTPException,Request
from to_db import insertdata
from schema import userschema
app=FastAPI()

@app.post('/createuser')
async def createUser(request:Request,data:userschema=None):
    request_data = await request.json()
    field_schema=userschema.__annotations__
    unknown_field=[x for x in request_data if x not in field_schema]
    print(unknown_field)
    if len(unknown_field) >0:
          return {
            "message":"Please Enter a valid Field",
            "ie":f"{[x for x in field_schema]}",
            "unkown_field":unknown_field
        }
    # data = userschema(**request_data)
    if data is None or data==None:
        raise HTTPException(status_code=205,detail="Please Enter a valid feild")   
    return insertdata(data)

if __name__=="__main__":
    import uvicorn
    uvicorn.run(app="main:app",host="localhost",reload=True)