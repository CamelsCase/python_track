class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        iceCreams = 0
        for i in costs:
            if coins-i>=0:
                coins-=i
                iceCreams+=1
            else:
                return iceCreams
        return len(costs)