class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 0
        leng = len(nums)
        if leng ==1:
            return 1
        fast = 1
        try:
            while fast<leng:
                if nums[slow]==nums[fast]:
                    fast+=1
                else:
                    nums[slow+1] = nums[fast]
                    slow +=1
            return slow+1
        except Exception:
            return slow+1
            