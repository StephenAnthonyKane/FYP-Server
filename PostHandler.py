from MongoDB import MongoDB
import json

class PostHandler:
    def __init__(self):
        self.DBConnection = MongoDB()

    def Handle(self, data):
        beaconsDict = self.Parse(data)
        self.Save(beaconsDict)

    def Parse(self, data):
        PostObject = json.loads(data)
        print(PostObject)
        return PostObject['Beacons']

    def Save(self, beaconsDict):
        self.DBConnection.SaveNewEnteries(beaconsDict)