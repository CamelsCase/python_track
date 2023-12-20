class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        x,y = points[0]
        travel_sec = 0
        for i in range(len(points)):
            xd = abs(x-points[i][0])
            yd = abs(y-points[i][1])
            x,y = points[i]
            travel_sec+=max(xd,yd)
        return travel_sec
        