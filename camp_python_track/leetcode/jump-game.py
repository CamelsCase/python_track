class Solution:
    def canJump(self, nums: List[int]) -> bool:
        leng = len(nums)
        ind = leng
        nums[-1]=1
        for i in range(leng-1,-1,-1):
            if nums[i]+i>=ind:
                ind = i
        return ind == 0 