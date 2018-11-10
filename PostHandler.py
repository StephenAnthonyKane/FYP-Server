from MongoDB import MongoDB
import json

class PostHandler:
    def __init__(self):
        self.DBConnection = MongoDB()

    def Handle(self, data):
        BeaconData = self.Parse(data)
        self.Save(BeaconData)

    def Parse(self, data):
        return json.loads(data)

    def Save(self, BeaconData):
        self.DBConnection.SaveNewEntry(BeaconData)