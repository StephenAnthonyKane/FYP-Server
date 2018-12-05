from MongoDB import MongoDB
from DBRetriever import DBRetriever
from urllib import parse

class GetHandler:
    def __init__(self):
        self.DBConnection = DBRetriever()

    def Handle(self, data):
        query = self.Parse(data)
        return self.Get(query)

    def Parse(self, urlParams):
        query = dict(qc.split("=") for qc in urlParams.split("&"))
        print(query)
        return query

    def Get(self, query):
        return self.DBConnection.GetBeaconData(query)
