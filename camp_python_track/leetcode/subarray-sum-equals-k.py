class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt = 0
        pre = [nums[0]]
        for j in range(1,len(nums)):
            pre.append(pre[j-1]+nums[j])
        dt = {0:1}
        for i in range(len(pre)):
            if pre[i]-k in dt:
                cnt+=dt[pre[i]-k]
            if not pre[i] in dt:
                dt[pre[i]] = 1
            else:
                dt[pre[i]] += 1
        return cnt
