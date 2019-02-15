from FileLogger import FileLogger
import time


class QueryBuilder:
    def __init__(self):
        self.Logger = FileLogger()

    def Build(self, arguments):
        query = self.GetFilter(arguments)
        return query

    def GetFilter(self, arguments):
        self.Logger.Info(arguments)
        query = {}
        for key in arguments:
            if key == 'Offset':
                #if (int(arguments[key])) == 0:
                    #continue
                query['Timestamp'] = {'$gte': (int(time.time()) - (int(arguments[key]) * 60) ) }
                continue

            query[key] = arguments[key]
        return query
            
