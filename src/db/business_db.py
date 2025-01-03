from pymongo import MongoClient
def get_db():
    client = MongoClient()
    return client.test_database

db = get_db()

def get_post():
    return db.posts.find()
    