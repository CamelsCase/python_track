class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        bs = [0 for i in range(len(flips)+2)]
        cnt = 0
        mx = 0
        inv =0
        start = 1
        for i in flips:
            bs[i]=1
            mx = max(mx,i)
            found = True
            for j in range(start,mx+1):
                if bs[j]==0:
                    start = j
                    found = False
                    break
            if found:
                start = mx
                cnt+=1
        return cnt