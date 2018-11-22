import pymongo
import json
from MongoQuerier import MongoQuerier

class MongoDB:
    def __init__(self):
        self.myclient = pymongo.MongoClient('mongodb://localhost:27017/')
        self.dataBase = self.myclient["mydatabase"]
        self.collection = self.dataBase["beacondata"]

        self.mongoQuerier = MongoQuerier(self.collection)

    def SaveNewEntry(self, beaconData):
        id = self.collection.insert_one(beaconData)
        print("Item inserted with id: "+ str(id))

    def SaveNewEnteries(self, beaconsDict):
        self.collection.insert_many(beaconsDict)
        print("Items inserted")

    def QueryDataBase(self, query):
        return self.mongoQuerier.loadAllForQuery(query)

    def LoadAllEntries(self):
        return self.mongoQuerier.loadAllEntries()


