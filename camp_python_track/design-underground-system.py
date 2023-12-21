class UndergroundSystem:

    def __init__(self):
        self.train = dict()
        self.times = dict()
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.train[id]=[stationName,t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if (self.train[id][0],stationName) not in self.times:
            self.times[(self.train[id][0],stationName)]=[t-self.train[id][1]]
        else:
            self.times[(self.train[id][0],stationName)].append(t-self.train[id][1])

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        leng=len(self.times[(startStation,endStation)])
        return sum(self.times[(startStation,endStation)])/leng
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)