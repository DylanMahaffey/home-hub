from typing import List
# from .db_connection import get_db
from bson.objectid import ObjectId
from ..models.list_models import UserList
from pymongo import MongoClient

client = MongoClient()
db = client.home_hub
user_lists = db.user_lists

async def all_lists() -> List[UserList]:
    return user_lists.find()

async def get_list_by_id(id: str) -> UserList:
    return user_lists.find_one({"_id": ObjectId(id)})

async def post_new_list(list: UserList) -> str:
    return str(user_lists.insert_one(list.__dict__).inserted_id)

async def update_list(list: UserList) -> bool:
    return True 

async def delete_list(list_id: str) -> bool:
    return True