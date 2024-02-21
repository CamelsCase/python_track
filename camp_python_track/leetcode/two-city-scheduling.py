class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key = lambda x:x[0]-x[1])
        sm = 0
        leng = len(costs)
        for i in range(leng):
            if i<leng//2:
                sm+=costs[i][0]
            else:
                sm+=costs[i][1]
        return sm