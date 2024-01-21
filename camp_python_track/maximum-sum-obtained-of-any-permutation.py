class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        ind = [0]*(len(nums)+1)
        for i in requests:
            ind[i[0]]+=1
            ind[i[1]+1]-=1
        pre = sorted(accumulate(ind),reverse=True)
        nums.sort()
        sm = 0
        for i in pre[:-1]:
            sm+=i*nums.pop()
        return sm%(10**9 + 7)