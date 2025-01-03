from fastapi import FastAPI
from src.routers.business import router as business_router

app = FastAPI()

app.include_router(business_router)

@app.get("/")
async def read_root():
    return  {"Hello": "World"}