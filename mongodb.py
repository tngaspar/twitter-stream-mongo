from pymongo import MongoClient

class TweetColection:
    def __init__(self, mongo_host: str, database_name: str, collection_name: str):
        client = MongoClient(mongo_host)
        db = client[database_name]
        self.colection = db[collection_name]
        
    @classmethod
    def from_auth_list(cls, mongo_auth: list):
        return cls(mongo_auth[0], mongo_auth[1], mongo_auth[2])
        
    def insert(self, dict: dict):
        self.colection.insert_one(dict)
        
    def select_all(self):
        cursor = self.colection.find()
        for record in cursor:
            print(record)
            
            
