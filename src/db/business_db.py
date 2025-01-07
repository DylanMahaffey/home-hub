from .db_connection import get_db
from ..models.business_models import BusinessProfile, Address, BusinessHours

db = get_db()

# def get_post():
    # return dumps(db.posts.find())