from ..scrapers.yellow_pages import get_business_locations

async def get_business_data(query: str, zip: str):
    return await get_business_locations(query, zip)