class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        pointer = 0
        seeker = 1
        while pointer<len(nums):
            if nums[pointer]!=0:
                pointer+=1
                seeker = pointer+1
            else:
                if seeker<len(nums) and nums[seeker]==0:
                    seeker+=1
                elif seeker<len(nums) and nums[seeker]!=0:
                    nums[pointer],nums[seeker] = nums[seeker],nums[pointer]
                    pointer+=1
                    seeker = pointer+1
                if seeker==len(nums):
                    
                    if nums[pointer]==nums[seeker-1]==0:
                        break
            