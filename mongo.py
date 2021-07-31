from pymongo import MongoClient

class MongoConnection:
    def __init__(self):
        client = MongoClient("mongodb://127.0.0.1:27023")
        self.db = client.urls

    def find(self, query = {}):
        db = self.db
        result = db.urls.find_one(query)
        print(result)
        return result
    
    def insert(self, record=None):
        if record is not None:
            db = self.db
            result = db.urls.insert_one(record)
            return result

        