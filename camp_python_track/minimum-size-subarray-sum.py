from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start = 0
        subarray_sum = 0
        min_length = float('inf')

        for end in range(len(nums)):
            subarray_sum += nums[end]

            while subarray_sum >= target:
                min_length = min(min_length, end - start + 1)
                subarray_sum -= nums[start]
                start += 1

        return min_length if min_length != float('inf') else 0