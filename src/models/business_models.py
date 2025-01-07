from typing import Optional
from pydantic import BaseModel

class Address(BaseModel):
    street: str
    city: str
    state: str
    zip: str
    
class BusinessHours(BaseModel):
    sunday: str
    monday: str
    tuesday: str
    wednesday: str
    thursday: str
    friday: str
    saturday: str

class BusinessProfile(BaseModel):
    _id: str
    name: str
    hours: BusinessHours
    url: Optional[str] = None
    yellow_pages_url: str
    address: Address
    

    