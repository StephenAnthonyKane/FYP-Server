from MongoDB import MongoDB
from DBSaver import DBSaver
from datetime import datetime
import json

class PostHandler:
    def __init__(self):
        self.DBConnection = DBSaver()

    def Handle(self, arguments):
        beaconsDict = self.Parse(arguments)
        self.Save(beaconsDict)

    def Parse(self, arguments):
        PostObject = arguments['Beacons']
        beaconDataDict = json.loads(PostObject)
        timestamp = datetime.now().strftime("%x") +" "+ datetime.now().strftime("%X")

        for beaconData in beaconDataDict:
            beaconData["Timestamp"] = timestamp
            print(beaconData)

        return beaconDataDict

    def Save(self, beaconsDict):
        self.DBConnection.SaveBeaconData(beaconsDict)