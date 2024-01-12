class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        pt1 = 0
        nums.sort()
        cnt = 0
        leng = len(nums)
        while pt1<leng-1:
            pt2 = pt1+1
            while pt2<leng:
                if nums[pt1]+nums[pt2]<target:
                    cnt+=1
                elif nums[pt1]+nums[pt2]>target:
                        break
                pt2+=1
            pt1+=1          
        return cnt
        #time-->(0(n**2))
        #space o(1)
