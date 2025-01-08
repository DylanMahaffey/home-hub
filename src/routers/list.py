from fastapi import APIRouter
from ..models.list_models import UserList
from ..controllers.list_controller import get_list_by_id, get_all_lists, add_new_list

router = APIRouter(
    prefix = "/lists"
)

@router.get("/list/{id}")
async def list(id: str):
    return await get_list_by_id(id)

@router.get('/')
async def all_lists():
    return await get_all_lists()

@router.post("/")
async def new_list(list: UserList):
    return await add_new_list(list)
