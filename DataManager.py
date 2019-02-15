from DBRetriever import DBRetriever
from FileLogger import FileLogger
from LocationCalculator import LocationCalculator
from QueryBuilder import QueryBuilder


class DataManager:
    def __init__(self):
        self.DBConnection = DBRetriever()
        self.Logger = FileLogger()
        self.Locator = LocationCalculator()
        self.QueryBuilder = QueryBuilder()

    def Manage(self, parameters):
        # BuildQuery
        query = self.QueryBuilder.Build(parameters)

        # IfDeviceID
        if 'DeviceID' in query:
            return self.GetDeviceLocation(query.pop('DeviceID'), query)

        # IfBeaconID
        if 'BeaconID' in query:
            self.Logger.Info('Datamanager: ' + str(query))
            return self.GetBeaconinformation('BeaconInformation', query)

    def GetDeviceLocation(self, deviceID, filter):
        nearByBeacons = self.Querydatabase(deviceID, filter)
        return self.Locator.Locate(nearByBeacons)

    def GetBeaconinformation(self, beaconInformation, filter):
        return self.Querydatabase(beaconInformation, filter)

    def Querydatabase(self, collectionName, filter):
        return self.DBConnection.QueryDatabase(collectionName, filter)
