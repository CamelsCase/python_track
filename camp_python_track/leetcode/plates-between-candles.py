class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        candles  = []
        for i in range(len(s)):
            if s[i]=="|":
                candles.append(i)
        ans = []
        for l,r in queries:
            x = bisect_left(candles,l)
            y = bisect_right(candles,r)-1
            ans.append(candles[y]-candles[x]-(y-x) if x<=y else 0)
        return ans
