class UndergroundSystem:

    def __init__(self):
        self.customer = {} # [id] = [station, checkin time]
        self.station = {} # [(start, end)] = [duration, times]

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.customer[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start, end, duration = self.customer[id][0], stationName, t-self.customer[id][1]
        if (start, end) not in self.station:
            self.station[(start, end)] = [0,0]
        self.station[(start, end)][0]+=duration
        self.station[(start, end)][1] += 1

    def getAverageTime(self, s: str, e: str) -> float:
        return self.station[(s, e)][0]/self.station[(s, e)][1]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)