import pymongo
from MongoDB import MongoDB
import json

class DBRetriever:
    def __init__(self,):
        self.connection= MongoDB('mongodb://localhost:27017/', "mydatabase")

    def GetBeaconData(self, beaconId):
        #Get all data from collection
        return self.connection.LoadAllEntries(beaconId)