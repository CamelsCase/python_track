class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        mn1 = 2**32
        mn2 = 2**32
        for i in nums:
            if i<mn1:
                mn1 = i
            if i>mn2:
                return True
            if i>mn1:
                mn2=i
        return False
            