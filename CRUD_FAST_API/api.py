from fastapi import FastAPI
import requests

from constant_crud import *
app = FastAPI()


@app.get("/get/user/list")
def getItems():
    try:
        list=[
            {
                'name':'Waseem',
                'age':24,
                'address':'MKD'
            }
        ]
        return list
    except Exception as e:
        print(type(e).__name__)
        return "Not found!"


@app.post("/set/user")
def setItems(user:User):
    try:
        user_info={
            'name':user.name,
            'address':user.address,
            'age':user.age
        }
        USERS_RECORD.update_one(user_info,upsert=True)
        
        return "Inserted successfully!"
    except Exception as e:
        print(type(e).__name__)
        return "Not found!"