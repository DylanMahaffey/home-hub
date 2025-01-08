from typing import List
from .db_connection import get_db
from bson.objectid import ObjectId
from ..models.list_models import ListItem

user_lists_items = get_db().list_item

async def get_list_item_by_id_db(id: str) -> ListItem:
    return user_lists_items.find_one({"_id": ObjectId(id)})

async def get_list_items_db(list_id: str) -> List[ListItem]:
    return user_lists_items.find({"list_id": list_id})

async def get_in_cart_items_db(list_id: str) -> List[ListItem]:
    return user_lists_items.find({"list_id": list_id, "in_cart": True})

async def post_list_item_db(list_item: ListItem) -> str:
    return str(user_lists_items.insert_one(list_item.__dict__).inserted_id)

async def update_list_item_db(id: str, list_item: ListItem) -> int:
    filter = {"_id": ObjectId(id)}
    update = {"$set": list_item.__dict__}
    return user_lists_items.update_one(filter, update).modified_count

async def delete_list_item_db(list_id: str) -> int:
    return user_lists_items.delete_one({"_id": ObjectId(list_id)})

async def delete_in_cart_itmes_db(list_id: str) -> int:
    return user_lists_items.delete_many({"list_id": list_id, "in_cart": True}).deleted_count