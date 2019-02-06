from MongoDB import MongoDB
from DBSaver import DBSaver
from FileLogger import FileLogger
import time
import json

class PostHandler:
    def __init__(self):
        self.DBConnection = DBSaver()
        self.Logger = FileLogger()

    def Handle(self, arguments):
        try:
            self.Logger.Info("POST request received")
            beaconsDict = self.Parse(arguments)
            self.Save(beaconsDict)
        except Exception as e:
            self.Logger.Error(e)

    def Parse(self, arguments):
        PostObject = arguments.value
        self.Logger.Info('Object Recived: ' + PostObject)
        josnObject=json.loads(PostObject)
        beaconDataDict = josnObject['Beacons']
        timestamp = int(time.time())
        self.Logger.Info(timestamp)

        for beaconData in beaconDataDict:
            beaconData["Timestamp"] = timestamp
            self.Logger.Info(beaconData)

        return beaconDataDict

    def Save(self, beaconsDict):
        self.Logger.Info("Saving Data")
        self.DBConnection.SaveBeaconData(beaconsDict)