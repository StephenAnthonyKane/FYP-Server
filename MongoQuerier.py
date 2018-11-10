import pymongo

class MongoQuerier:
    def __init__(self, collection):
        self.collection= collection

    def loadAllEntries(self):
        return self.collection.find()