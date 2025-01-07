from fastapi import FastAPI
from src.routers.business import router as business_router
from src.routers.list import router as list_router
from src.routers.list_item import router as list_item_router

app = FastAPI()

app.include_router(business_router)
app.include_router(list_router)
app.include_router(list_item_router)

@app.get("/")
async def read_root():
    return  {"Hello": "World"}