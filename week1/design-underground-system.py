class UndergroundSystem:

    def __init__(self):
        
        self.people = {}
        self.stations = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.people[id] = (stationName, t)


    def checkOut(self, id: int, stationName: str, t: int) -> None:
        initialStation = self.people[id][0]
        startTime =self.people[id][1]
        if initialStation in self.stations:
            if stationName in self.stations[initialStation]:
                self.stations[initialStation][stationName][0] += (t - startTime)
                self.stations[initialStation][stationName][1] += 1
            else:
                self.stations[initialStation][stationName] = [(t - startTime), 1]
        else:
            self.stations[initialStation] = {stationName:[t - startTime, 1]}
        
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.stations[startStation][endStation][0] / self.stations[startStation][endStation][1]
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)