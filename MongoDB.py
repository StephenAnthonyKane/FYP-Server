import pymongo
import json
from bson.json_util import dumps

class MongoDB:
    def __init__(self, clientURL, databaseName):
        self.myclient = pymongo.MongoClient(clientURL)
        self.dataBase = self.myclient[databaseName]

    def SaveNewEntry(self, collectionName, data):
        self.GetConnection(collectionName)
        self.collection.insert_one(data)
        print("Item inserted with id: "+ str(id))

    def SaveNewEnteries(self, collectionName, dataDict):
        self.GetConnection(collectionName)
        self.collection.insert_many(dataDict)
        print("Items inserted")

    def loadAllEntries(self, collectionName):
        self.GetConnection(collectionName)
        cursor = self.collection.find()
        return dumps(cursor)

    def QueryCollection(self, collectionName, query):
        self.GetConnection(collectionName)
        cursor = self.collection.find(query)
        return dumps(cursor)

    def GetConnection(self, collectionName):
        self.collection = self.dataBase[collectionName]