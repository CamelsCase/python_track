class Solution:
    def hIndex(self, citations: List[int]) -> int:
        leng = len(citations)
        l = 0
        r = leng

        while l < r:
            md = (l + r +1) // 2  
            if citations[leng - md] >= md:
                l = md
            else:
                r = md - 1
        return l
            