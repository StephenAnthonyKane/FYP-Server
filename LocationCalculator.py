from FileLogger import FileLogger

class LocationCalculator:
    def __init__(self):
        self.Logger = FileLogger()

    def Locate(self, RetrivedData):
        try:
            self.Logger.Info(RetrivedData)
            return self.GetRSS(RetrivedData)
        except Exception as e:
            self.Logger.Error("ERROR in LocationCalculator: "+str(e))

    def GetRSS(self, RetrivedData):
        beaconsRSS = []
        for beacon in RetrivedData:
            if not any(b['UID'] == beacon['UID'] for b in beaconsRSS):

                beaconsFound = [x for x in RetrivedData if x['UID'] == beacon['UID']]

                totalRSS =0
                for b in beaconsFound:
                    if "RSS" in b:
                        totalRSS += int(b['RSS'])
            
                newBeaconRSS = {"UID": beacon['UID'], "RSS": totalRSS/len(beaconsFound)}
                beaconsRSS.append(newBeaconRSS)

        self.Logger.Info(beaconsRSS)
        return beaconsRSS

