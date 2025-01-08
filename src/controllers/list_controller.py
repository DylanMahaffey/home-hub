from bson.json_util import dumps
from typing import List
from ..models.list_models import UserList, ListItem
from ..db.list_db import get_list_by_id_db, all_lists_db, post_new_list_db
from ..db.list_item_db import get_list_item_by_id_db, get_list_items_db, get_in_cart_items_db, post_list_item_db, update_list_item_db, delete_list_item_db, delete_in_cart_itmes_db

#UserList handlers
async def get_list_by_id(id: str) -> UserList:
    return dumps(await get_list_by_id_db(id))

async def get_all_lists() -> List[UserList]:
    return dumps(await all_lists_db())

async def add_new_list(list: UserList) -> str:
    return await post_new_list_db(list)

#ListItem handlers
async def get_list_item_by_id(id: str) -> ListItem:
    return dumps(await get_list_by_id_db(id))

async def get_list_items(list_id: str) -> List[ListItem]:
    return dumps(await get_list_items_db(list_id))

async def post_list_item(list_item: ListItem) -> str:
    return await post_list_item_db(list_item)

async def update_list_item(id: str, list_item: ListItem) -> int:
    return await update_list_item_db(id, list_item)

async def update_multiple_items(list_items: List[ListItem]) -> int:
    return True

async def delete_list_item(id: str) -> int:
    return await delete_list_item_db(id)

async def delete_multiple_list_items(list_item_ids: List[str]) -> int:
    return True

async def complete_list_litems(list_id: str) -> int:
    return await delete_in_cart_itmes_db(list_id)