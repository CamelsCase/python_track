class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        out = [0]*52
        for i in ranges:
            out[i[0]] += 1
            out[i[1]+1] -= 1
        prefix = [out[0]]
        
        for i in range(1,51):
            prefix.append(prefix[i-1]+out[i])
        for i in range(left,right+1):
            if prefix[i] ==0:
                return False
        return True