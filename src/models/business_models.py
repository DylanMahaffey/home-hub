from typing import Optional
from pydantic import BaseModel

class Address(BaseModel):
    street: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    zip: Optional[str] = None
    
class BusinessHours(BaseModel):
    sunday: Optional[str] = None
    monday: Optional[str] = None
    tuesday: Optional[str] = None
    wednesday: Optional[str] = None
    thursday: Optional[str] = None
    friday: Optional[str] = None
    saturday: Optional[str] = None

class BusinessProfile(BaseModel):
    _id: Optional[str]
    ypid: Optional[str] = None
    name: Optional[str] = None
    hours: Optional[BusinessHours] = None
    url: Optional[str] = None
    yellow_pages_url: Optional[str] = None
    address: Optional[Address] = None
    

    