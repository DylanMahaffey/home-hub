from fastapi import APIRouter
from bson.json_util import dumps
from ..models.list_models import UserList
from ..db.list_db import get_list_by_id, all_lists, post_new_list

router = APIRouter(
    prefix = "/lists"
)

@router.get("/list/{id}")
async def get_list(id: str):
    return dumps(await get_list_by_id(id))

@router.get('/')
async def get_all_lists():
    return dumps(await all_lists())

@router.post("/")
async def new_list(list: UserList):
    return await post_new_list(list)
