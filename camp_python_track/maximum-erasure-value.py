class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        freq = Counter()
        st = 0 
        en = 0
        sm = 0
        mx = 0
        while st<len(nums):
            while en<len(nums) and freq[nums[en]]<1:
                freq[nums[en]]+=1
                sm+=nums[en]
                en+=1
            mx = max(sm,mx)
            if en==len(nums):
                break
            while st<len(nums) and freq[nums[en]]>=1:
                freq[nums[st]]-=1
                sm-=nums[st]
                st+=1
        return mx
        #the time complexity o(n)
        #space complexity o(1)