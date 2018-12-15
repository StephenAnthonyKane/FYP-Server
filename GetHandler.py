from MongoDB import MongoDB
from DBRetriever import DBRetriever

class GetHandler:
    def __init__(self):
        self.DBConnection = DBRetriever()

    def Handle(self, arguments):
        query = self.Parse(arguments)
        return self.Get(query)

    def Parse(self, arguments):
        query = arguments["UID"]
        print(query)
        return query

    def Get(self, query):
        return self.DBConnection.GetBeaconData(query)
