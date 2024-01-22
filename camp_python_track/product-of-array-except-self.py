class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [nums[0]]
        suffix = [nums[-1]]
        leng = len(nums)
        for i in range(1, leng):
            prefix.append(prefix[i-1] * nums[i])
            suffix.append(suffix[-1] * nums[leng-i-1])
        suffix = suffix[::-1]
        return [(prefix[i-1] if i > 0 else 1) * (suffix[i+1] if i < leng-1 else 1) for i in range(leng)]

