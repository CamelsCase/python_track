class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        ls = [0]*1001
        for i in trips:
            ls[i[1]]+= i[0]
            ls[i[2]]-= i[0]
            if ls[i[1]]>capacity:
                return False
        pre = list(accumulate((ls)))
        for i in pre:
            if i>capacity:
                return False
        return True