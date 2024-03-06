class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        _min = float('inf')
        if nums[0] < nums[-1]:
            return nums[0] 
        while left <= right:
            mid = (left + right)//2
            if nums[left] <= nums[mid]:
                _min = min(_min, nums[left])
                left = mid+1
                _min = min(_min,nums[mid])
                continue
            else:
                right = mid-1
                _min = min(_min,nums[mid])
        return _min