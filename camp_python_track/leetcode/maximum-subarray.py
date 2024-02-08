class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
    #this block of code help to find the prefix sum
    #start
        pre = [nums[0]]
        for i in range(1,len(nums)):
            pre.append(pre[i-1]+nums[i])  
    #end
    
    #the below code help to get the next maximum starting from some index i  
    #start
        next_max = [pre[-1]]
        for i in range(-2,-(len(pre)+1),-1):
            next_max.append(max(next_max[-1],pre[i]))
        next_max = next_max[::-1]
    #end

        mx = -10**5
        for i in range(len(pre)-1):
            mx1 = next_max[i+1]-pre[i]
            mx = max(pre[i],mx,mx1)
        mx = max(mx,pre[-1])
        return mx