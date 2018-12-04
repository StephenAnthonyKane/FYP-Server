import pymongo
from MongoDB import MongoDB
import json

class DBSaver:
    def __init__(self,):
        self.connection= MongoDB('mongodb://localhost:27017/', "mydatabase")

    def SaveBeaconData(self, beaconDataDict):
        #Save into beacon collection
        for beaconData in beaconDataDict:
            self.connection.SaveNewEntry(str(beaconData['UID']), beaconData)
        #Save into master
        self.connection.SaveNewEnteries("beacondata", beaconDataDict)
        #Save into timed collection
