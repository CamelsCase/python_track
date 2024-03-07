class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def check(ts):
            sm = 0
            for i in nums:
                sm+=ceil(i/ts)
                if sm>threshold:
                    break
            return sm<=threshold
        left = 1
        right  = max(nums)
        while left<=right:
            mid = (left+right)//2
            if check(mid):
                right = mid-1
            else:
                left = mid + 1
        return left
