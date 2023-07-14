from db import engine
from models import User
from sqlalchemy.dialects.mysql import insert
from sqlmodel import select


def insertdata(data):
    data=dict(data)
    with engine.connect() as connection:
        in_st=insert(User).values(data)
        select_stmt = select(User).where(User.email == data['email'])
        existing_user = connection.execute(select_stmt).fetchone()
        print(existing_user,"exits")
        print(type(existing_user))
        if existing_user:
            return {"message": "Email already exists"}
        update_stmt = in_st.on_duplicate_key_update(in_st.inserted)
        results = connection.execute(update_stmt)
        return {
            "message":"User Created Sucessfully",
            "details":data
        }


def checklogin(data):
    with engine.connect() as connection:
        data=dict(data)
        check_data=select(User).where(User.email==data['email'] and User.password==data['password'])
        userfound=connection.execute(check_data).fetchone()
        if userfound:
            return {
                "message":"Successfully login"
            }
        else:
            return {
                "message":"user not found"
            }