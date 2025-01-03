from fastapi import APIRouter
from ..db.business_db import get_post
from bson.json_util import dumps, loads 

router = APIRouter(
    prefix = "/business"
)

@router.get("/")
async def root():
    post = list(get_post())
    return dumps(post)

