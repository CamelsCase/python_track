class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        mx = min(nums)
        sm = sum(nums[:k])
        for i in range(len(nums)-k+1):
            if i>0:
                sm = sm+nums[i+k-1]-nums[i-1]
                av = (sm)/k
            else:
                av =sm/k
            if av>mx:
                mx=av
        return mx