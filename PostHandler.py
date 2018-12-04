from MongoDB import MongoDB
from DBSaver import DBSaver
from datetime import datetime
import json

class PostHandler:
    def __init__(self):
        self.DBConnection = DBSaver()

    def Handle(self, data):
        beaconsDict = self.Parse(data)
        self.Save(beaconsDict)

    def Parse(self, data):
        PostObject = json.loads(data)
        beaconDataDict = PostObject['Beacons']    
        timestamp = datetime.now().strftime("%x") +" "+ datetime.now().strftime("%X")

        for beaconData in beaconDataDict:
            beaconData["Timestamp"] = timestamp

        return beaconDataDict

    def Save(self, beaconsDict):
        self.DBConnection.SaveBeaconData(beaconsDict)