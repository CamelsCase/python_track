class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        x,y = points[0]
        travel_sec = 0
        for i in range(len(points)):
            travel_sec+=max(abs(x-points[i][0]),abs(y-points[i][1]))
            x,y = points[i]
        return travel_sec
        