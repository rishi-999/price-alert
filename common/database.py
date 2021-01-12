import pymongo
from typing import Dict

class Database:

    URI = "mongodb://127.0.0.1:27017/pricing"
    DATABASE = pymongo.MongoClient(URI).get_database()

    @staticmethod
    def insert(collection: str, data: Dict):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection: str, query: Dict) -> pymongo.cursor:
        return Database.DATABASE[collection].find(query)

    @classmethod
    def find_one(cls,collection, query):
        return Database.DATABASE[collection].find_one(query)

    @staticmethod
    def update(collection,query,data) -> None:
        Database.DATABASE[collection].update(query,data, upsert=True)

    @staticmethod
    def remove(collection,query):
        return Database.DATABASE[collection].remove(query)