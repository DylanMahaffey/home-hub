from fastapi import APIRouter
from bson.json_util import dumps, loads 
from ..scrapers.yellow_pages import get_business_locations

router = APIRouter(
    prefix = "/business"
)    

@router.get("/locations/")
async def get_locations(query: str, zip: str):
    locations = get_business_locations(query, zip)
    return locations

