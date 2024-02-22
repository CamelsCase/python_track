class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        pre = [0]*(len(nums)+1)

        #this will mark the ranges
        for start,end in requests:
            pre[start]+=1
            pre[end+1]-=1

        #this will compute the prefix sum
        for i in range(1,len(nums)+1):
            pre[i]+=pre[i-1]

        # reverse sort the prefix sum and multiply the maximum range intersection with the maximum value in the list
        pre.sort(reverse = True)
        nums.sort()
        ans = 0
        for i in pre:
            if i!=0:
                ans+=i*nums.pop()
            else:#since the prefix sum is reverse sorted if we find zero we should stop 
                return ans%(10**9 + 7)
        return ans%(10**9 + 7)
        #space complexity O(N)
        #time complexity O(N)


        