from FileLogger import FileLogger
from DataManager import DataManager



class GetHandler:
    def __init__(self):
        self.DataManager = DataManager()
        self.Logger = FileLogger()

    def Handle(self, arguments):
        try:
            self.Logger.Info("GET request received")
            parameters = self.Parse(arguments)
            return self.GetData(parameters)
        except Exception as e:
            self.Logger.Error(e)

    def Parse(self, arguments):
        params = {}
        for key in arguments.keys():
            params[key] = arguments[key].value
        return params

    def GetData(self, parameters):
        return self.DataManager.Manage(parameters)
