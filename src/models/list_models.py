from pydantic import BaseModel
from typing import Optional
from .business_models import BusinessProfile


class UserList(BaseModel):
    _id: Optional[str]
    title: str
    # business: Optional[BusinessProfile]
    
class ListItem(BaseModel):
    _id: Optional[str]
    list_id: str
    text: str
    in_cart: bool = False