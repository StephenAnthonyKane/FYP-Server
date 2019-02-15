from MongoDB import MongoDB
from FileLogger import FileLogger
from bson.json_util import dumps
import json


class DBRetriever:
    def __init__(self):
        self.connection = MongoDB('mongodb://localhost:27017/', "mydatabase")
        self.Logger = FileLogger()

    def QueryDatabase(self, collectionName, filter):
        self.Logger.Info('CollectionName: ' + collectionName + ' Query: '+str(filter))
        cursor = self.connection.QueryCollection(collectionName, filter)
        #cursor = self.connection.LoadAllEntries(collectionName)
        return self.ParseCursor(cursor)

    def ParseCursor(self, cursor):
        cursorList = list(cursor)
        parsedData = []
        for beaconCursor in cursorList:
            beaconJSON = dumps(beaconCursor)
            beaconObject = json.loads(beaconJSON)
            parsedData.append(beaconObject)

        self.Logger.Info('ReturnedData: '+str(parsedData))
        return parsedData
