from fastapi import APIRouter
from typing import List
from ..models.list_models import ListItem
from ..controllers.list_controller import get_list_item_by_id ,get_list_items,post_list_item,update_list_item,update_multiple_items,delete_list_item,delete_multiple_list_items,complete_list_litems

router = APIRouter(
    prefix = "/list-items"
)

@router.get("/list-item/{id}")
async def list_item(id: str):
    return await get_list_item_by_id(id)

@router.get("/{list_id}")
async def list_items(list_id: str):
    return await get_list_items(list_id)

@router.post("/")
async def post_item(list_item: ListItem):
    return await post_list_item(list_item)

@router.put("/update-item/{item_id}")
async def patch_list_item(item_id: str, list_item: ListItem):
    return await update_list_item(item_id, list_item)

@router.put("/")
async def update_items(list_items: List[ListItem]):
    return await update_multiple_items(list_items)

@router.delete("/")
async def delete_item(id: str):
    return await delete_list_item(id)

@router.delete("/delete-items")
async def delete_items(list_item_ids: List[str]):
    return await delete_multiple_list_items(list_item_ids)

@router.delete("/complete-items/{list_id}")
async def complete_items(list_id: str):
    return await complete_list_litems(list_id)