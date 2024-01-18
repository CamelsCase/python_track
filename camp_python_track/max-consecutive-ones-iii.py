class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        if k >= nums.count(0):
            return len(nums)
        p1 = 0
        p2 = 0
        mx = 0
        zero_count = 0
        while p2 < len(nums):
            if nums[p2] == 0:
                zero_count += 1
            while zero_count > k:
                if nums[p1] == 0:
                    zero_count -= 1
                p1 += 1
            p2 += 1
            current_length = p2 - p1

            if current_length > mx:
                mx = current_length

        return mx