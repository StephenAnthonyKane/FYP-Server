from FileLogger import FileLogger

class LocationCalculator:
    def __init__(self):
        self.Logger = FileLogger()

    def Locate(self, RetrivedData):
        return self.GetRSS(RetrivedData)

    def GetRSS(self, RetrivedData):
        beaconsRSS = []
        for beacon in RetrivedData:
            if not any(b['UID'] == beacon['UID'] for b in beaconsRSS):

                beaconsFound = [x for x in RetrivedData if x['UID'] == beacon['UID']]

                totalRSS =0
                for b in beaconsFound:
                    totalRSS += int(b['RSS'])
            
                newBeaconRSS = {"UID": beacon['UID'], "RSS": totalRSS/len(beaconsFound)}
                beaconsRSS.append(newBeaconRSS)

        self.Logger.Info(beaconsRSS)
        return beaconsRSS

