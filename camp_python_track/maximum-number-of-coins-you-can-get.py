class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse = True)
        coin = 0
        lg = 0
        for i in range(1,len(piles),2):
            if lg>=len(piles)-1:
                break
            coin+=piles[i]
            lg+=3
        return coin