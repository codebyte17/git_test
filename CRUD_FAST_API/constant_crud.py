from pymongo import MongoClient
from pydantic import BaseModel
from typing import Union


class User(BaseModel):
    name:str
    age:int
    address: Union[str,None]=None

client= MongoClient("mongodb://localhost:27017/")

USER_DATA=client.user_records
USERS_RECORD=USER_DATA['user_records']