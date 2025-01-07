from fastapi import APIRouter
from bson.json_util import dumps
from typing import List
from ..models.list_models import ListItem
from ..db.list_item_db import get_list_item, get_list_items, get_in_cart_items, post_list_item, update_list_item, delete_list_item

router = APIRouter(
    prefix = "/list-items"
)

@router.get("/item/{id}")
async def get_item(id: str):
    return dumps(get_list_item(id))

@router.get("/{list_id}")
async def get_items(list_id: str):
    return dumps(get_list_items(list_id))

@router.post("/")
async def post_item(list_item: ListItem):
    return post_list_item(list_item)

@router.put("/")
async def update_item(list_item: ListItem):
    return update_list_item(list_item)

# @router.put("/update-items")
# async def update_items(list_items: List[ListItem]):
#     return update_list_item(list_items)

@router.delete("/")
async def delete_item(id: str):
    return delete_list_item(id)

@router.delete("/delete-items")
async def delete_items(list_item_ids: List[str]):
    try:
        for id in list_item_ids:
            delete_list_item(id)
            return True
    except:
        return False

@router.delete("/complete-items")
async def delete_items(list_id: str):
    try:
        completed_items = get_in_cart_items(list_id)
        item_ids = map(lambda i: i._id, completed_items)
        for id in item_ids:
            delete_list_item(id)
        return True
    except:
        return False