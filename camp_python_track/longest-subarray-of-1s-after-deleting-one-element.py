class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        sp = "".join(map(str,nums)).split("0")
        mx = 0
        for i in range(len(sp)-1):
            leng = len(sp[i])+len(sp[i+1])
            if leng>mx:
                mx = leng
        return mx if 0 in nums else len(nums)-1