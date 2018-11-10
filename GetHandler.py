from MongoDB import MongoDB

class GetHandler:
    def __init__(self):
        self.DBConnection = MongoDB()

    def Handle(self, data):
        beaconId = self.Parse(data)
        return self.Get(beaconId)

    def Parse(self, data):
        return data

    def Get(self, id):
        return self.DBConnection.loadAllEntries()
