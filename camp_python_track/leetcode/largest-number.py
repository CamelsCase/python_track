class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        mx = 0
        mn = 10**9
        for i in range(len(nums)):
            nums[i] = str(nums[i])
            if len(nums[i])>mx:
                mx = len(nums[i])
        repeat = mx
        nums.sort(key = lambda x: str(x)*repeat,reverse = True)
        out = "".join(nums)
        return out if out[0]!="0" else "0"