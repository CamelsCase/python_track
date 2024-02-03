class Solution:
    def maxScore(self, s: str) -> int:
        zeros = [1-int(i) for i in s]
        ones =  [int(i) for i in s][::-1]
        prez = list(accumulate(zeros))
        preo = list(accumulate(ones))[::-1]
        print(preo)
        print(prez)
        mx = 0
        for i in range(1,len(s)):
            mx = max(mx,prez[i-1]+preo[i])
        return mx