class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums =  sorted(nums)
        last = nums[-1]
        for i in range(last):
            if i not in nums:
                return i
        return last+1