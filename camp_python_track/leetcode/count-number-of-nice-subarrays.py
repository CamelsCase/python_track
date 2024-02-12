class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        dt = defaultdict(int)
        dt[0] = 1
        nums[0]%=2
        cnt =  dt[nums[0]-k] if nums[0]-k in dt else 0
        dt[nums[0]]+=1
        for i in range(1,len(nums)):
            nums[i] = nums[i]%2+nums[i-1]
            if nums[i]-k in dt:
                cnt+=dt[nums[i]-k]
            dt[nums[i]]+=1
        return cnt
        #TIME COMPLEXITY O(N)
        #SPACE COMPLEXITY O(N)