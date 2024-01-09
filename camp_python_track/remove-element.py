class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        cnt = nums.count(val)
        rem = 0
        i = 0
        while cnt and i<len(nums):
            if nums[i]==val:
                nums.pop(i)
                cnt-=1
            else:
                i+=1
        return len(nums)