import pymongo
from bson.json_util import dumps

class MongoQuerier:
    def __init__(self, collection):
        self.collection= collection

    def loadAllEntries(self):
        cursor = self.collection.find()
        print(dumps(cursor))
        return dumps(cursor)

    def loadAllForQuery(self, query):
        cursor = self.collection.find(query)
        return dumps(cursor)