from typing import List
from .db_connection import get_db
from bson.objectid import ObjectId
from ..models.list_models import UserList
from pymongo import MongoClient

user_lists = get_db().user_lists

async def all_lists_db() -> List[UserList]:
    return user_lists.find()

async def get_list_by_id_db(id: str) -> UserList:
    return user_lists.find_one({"_id": ObjectId(id)})

async def post_new_list_db(list: UserList) -> str:
    return str(user_lists.insert_one(list).inserted_id)

async def update_list_db(list: UserList) -> bool:
    return True 

async def delete_list_db(list_id: str) -> bool:
    return True