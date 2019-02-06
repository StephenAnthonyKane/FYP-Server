from MongoDB import MongoDB
from QueryBuilder import QueryBuilder
from FileLogger import FileLogger
from bson.json_util import dumps
import json


class DBRetriever:
    def __init__(self):
        self.connection = MongoDB('mongodb://localhost:27017/', "mydatabase")
        self.QueryBuilder = QueryBuilder()
        self.Logger = FileLogger()

    def GetBeaconData(self, parameters):
        queryObject = self.QueryBuilder.Build(parameters)
        self.Logger.Info('Query: '+str(queryObject['Filter']))
        cursor = self.connection.QueryCollection(queryObject['CollectionName'], queryObject['Filter'])
        return self.ParseCursor(cursor)

    def GetAllBeaconData(self, beaconId):
        return self.connection.LoadAllEntries(beaconId)

    def ParseCursor(self, cursor):
        cursorList = list(cursor)
        parsedData = []
        for beaconCursor in cursorList:
            beaconJSON = dumps(beaconCursor)
            beaconObject = json.loads(beaconJSON)
            parsedData.append(beaconObject)
        return parsedData
