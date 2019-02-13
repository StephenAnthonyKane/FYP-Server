from FileLogger import FileLogger
import time


class QueryBuilder:
    def __init__(self):
        self.Logger = FileLogger()

    def Build(self, arguments):
        queryObject = {}
        queryObject['CollectionName'] = arguments.pop('DeviceID')
        queryObject['Filter'] = self.GetFilter(arguments)
        return queryObject

    def GetFilter(self, arguments):
        self.Logger.Info(arguments)
        query = {}
        for key in arguments:
            if key == 'Offset':
                if (int(arguments[key])) == 0:
                    continue
                query['Timestamp'] = {'$gte': (int(time.time()) - (int(arguments[key]) * 60) ) }
                continue
            query[key] = arguments[key]
        return query
            
