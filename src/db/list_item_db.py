from typing import List
from .db_connection import get_db
from bson.objectid import ObjectId
from ..models.list_models import ListItem

db = get_db()
user_lists_items = db.lists_item

def get_list_items(list_id: str) -> List[ListItem]:
    return user_lists_items.find({"list_id": ObjectId(list_id)})

def get_list_item(id: str) -> ListItem:
    return user_lists_items.find_one({"_id": ObjectId(id)})

def get_in_cart_items(list_id) -> List[ListItem]:
    return user_lists_items.find({"list_id": ObjectId(list_id), "in_cart": True})

def post_list_item(list_item: ListItem) -> str:
    return user_lists_items.insert_one(list_item).inserted_id

def update_list_item(list_item: ListItem) -> bool:
    return True

def delete_list_item(list_id: str) -> bool:
    return True