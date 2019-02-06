from FileLogger import FileLogger
import time


class QueryBuilder:

    def Build(self, arguments):
        queryObject = {}
        queryObject['CollectionName'] = arguments.pop('DeviceID')
        queryObject['Filter'] = self.GetFilter(arguments)
        return queryObject

    def GetFilter(self, arguments):
        query = {}
        for key in arguments:
            if key == 'Offset':
                query['Timestamp'] = '{$gte:' + str(int(time.time()) - (int(arguments[key]) * 60) ) + '}'
                continue
            query[key] = arguments[key]
        return query
            
