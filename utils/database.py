
import pymongo

class DbConnection():
    def __init__(self, host, port, database):
        self.client = pymongo.MongoClient(host, port)
        self.db = self.client[database]

    def insert_many(self,collection,data):
        col = self.db[collection]
        result = col.insert_many(data)
        return result.inserted_ids
    
    def insert_one(self,collection,data):
        col = self.db[collection]
        result = col.insert_one(data)
        return result.inserted_id
    
    def find_data_byId(self, collection, query={}):
        col = self.db[collection]
        result = col.find_one(query)
        return result
    
    def delete_one(self, collection, query):
        col = self.db[collection]
        result = col.delete_one(query)
        return result
    
    def update_one(self, collection, query, new_data):
        col = self.db[collection]
        result = col.update_one(query, {"$set": new_data})
        return result.modified_count

    def show_data(self, collection):
        col = self.db[collection]
        results = col.find()
        return list(results)