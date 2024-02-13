class Solution:
    def sortColors(self, nums: List[int]) -> None:
        st = 0
        en = 0
        find = 0
        while st<len(nums):
            while  st<len(nums) and en<len(nums):
                if nums[en]==find:
                    nums[st],nums[en]=nums[en],nums[st]
                    st+=1
                en+=1      
            find+=1
            en = st
        return nums