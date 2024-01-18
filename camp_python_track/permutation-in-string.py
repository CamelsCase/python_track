class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq1 = Counter(s1)
        leng = sum(freq1.values())
        for i in range(len(s2)):
            if Counter(s2[i:i+leng])==freq1:
                return True
        return False