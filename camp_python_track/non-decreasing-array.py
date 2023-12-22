class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        fail = 0
        for i in range(1,len(nums)):
            if nums[i-1]>nums[i]:
                if fail==1:
                    return False
                fail+=1
                if i>=2 and nums[i-2]>nums[i]:
                    nums[i]=nums[i-1]
        return True