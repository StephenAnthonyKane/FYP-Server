import pymongo
from bson.json_util import dumps

class MongoQuerier:
    def __init__(self, collection):
        self.collection= collection

    def loadAllEntries(self):
        cursor = self.collection.find()
        print(dumps(cursor))
        return dumps(cursor)

    def loadAllForUid(self, uid):
        cursor = self.collection.find({ "UID": uid })
        return dumps(cursor)