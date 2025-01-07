from pydantic import BaseModel
from typing import Optional
from .business_models import BusinessProfile


class UserList(BaseModel):
    _id: Optional[str]
    title: Optional[str]
    # business: Optional[BusinessProfile]
    
class ListItem(BaseModel):
    _id: Optional[str]
    list_id: Optional[str]
    text: Optional[str]
    in_cart: Optional[bool]