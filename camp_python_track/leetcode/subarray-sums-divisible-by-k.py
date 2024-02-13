class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        cnt = 0
        dt = defaultdict(int)
        dt[0] = 1
        cnt = dt[nums[0]%k] if nums[0]%k in dt else 0
        dt[nums[0]%k]+=1
        for i in range(1,len(nums)):
            nums[i]+=nums[i-1]
            if nums[i]%k in dt:
                cnt+=dt[nums[i]%k]
            dt[nums[i]%k]+=1
        return cnt
        #TIME COMPLEXITY O(N)
        #SPACE COMPLEXITY O(N)