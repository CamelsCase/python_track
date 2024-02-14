class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x:x[1])
        print(points)
        arrow1 = 0
        # cnt = 0
        arrow2 = 0
        arrows = 0
        while arrow1<len(points):
            while arrow2<len(points) and  points[arrow1][1]>=points[arrow2][0]:
                    arrow2+=1
                    # cnt+=1
            arrow1 = arrow2
            arrows+=1
        return arrows