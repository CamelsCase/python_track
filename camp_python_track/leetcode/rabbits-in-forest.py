class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        dt = defaultdict(int)
        cnt = 0
        for i in answers:
            dt[i]+=1
        for i in dt:
            cnt+=(i+1)*int(ceil(dt[i]/(i+1)))
        return cnt
        