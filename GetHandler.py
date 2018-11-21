from MongoDB import MongoDB

class GetHandler:
    def __init__(self):
        self.DBConnection = MongoDB()

    def Handle(self, data):
        beaconId = self.Parse(data)
        return self.Get(beaconId)

    def Parse(self, query):
        print(query)
        #query_components = dict(qc.split("=") for qc in query.split("&"))
        #print(query_components)
        return query

    def Get(self, id):
        return self.DBConnection.QueryDataBase(id)
