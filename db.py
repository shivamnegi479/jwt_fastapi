from urllib.parse import quote_plus
from sqlalchemy.engine import create_engine
from models import User
import json
with open('config.json','r') as e:
    data=json.load(e)
user=data["user"]
password=data["password"]
database=data["database"]
pswd=quote_plus(password)
db_url= f"mysql://{user}:{pswd}@localhost:3306/{database}"
try:
    engine=create_engine(db_url)
    conn=engine.connect()
    if conn:
        print("connect Successfully")
except :
    print("Not connected")

User.metadata.create_all(bind=engine)