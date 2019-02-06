from DBRetriever import DBRetriever
from FileLogger import FileLogger
from LocationCalculator import LocationCalculator


class GetHandler:
    def __init__(self):
        self.DBConnection = DBRetriever()
        self.Logger = FileLogger()
        self.Locator = LocationCalculator()

    def Handle(self, arguments):
        try:
            self.Logger.Info("GET request received")
            parameters = self.Parse(arguments)
            RetrivedData = self.GetData(parameters)
            beaconRSS = self.Locate(RetrivedData)
            return beaconRSS
        except Exception as e:
            self.Logger.Error(e)

    def Parse(self, arguments):
        params = {}
        for key in arguments.keys():
            params[key] = arguments[key].value
        return params

    def GetData(self, parameters):
        return self.DBConnection.GetBeaconData(parameters)

    def Locate(self, RetrivedData):
        return self.Locator.Locate(RetrivedData)
