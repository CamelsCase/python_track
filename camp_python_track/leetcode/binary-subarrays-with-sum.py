class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        dt  = defaultdict(int)
        dt[0] = 1 
        cnt = dt[nums[0]-goal] if nums[0]-goal in dt else 0
        dt[nums[0]]+=1
        for i in range(1,len(nums)):
            nums[i]+=nums[i-1]
            if nums[i]-goal in dt:
                cnt+=dt[nums[i]-goal]
            dt[nums[i]]+=1
        return cnt
        #TIME COMPLEXITY O(N)
        #SPACE COMPLEXITY IS LINEAR SINCE WE HAVE BINARY NUMBER AS THE KEY.SO O(1)