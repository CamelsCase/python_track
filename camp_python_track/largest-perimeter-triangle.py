class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        leng = len(nums)
        nums.sort()
        out = 0
        for i in range(leng-2):
            if sum(nums[i:i+2])>nums[i+2]:
                out = max(out,nums[i]+nums[i+1]+nums[i+2])       
        return out