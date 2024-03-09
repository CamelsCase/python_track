class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        leng = len(nums)
        cnt = 0
        for i in range(leng):
            st = i
            en = bisect_right(nums,target-nums[i])
            if en>=leng:
                cnt+=2**(leng-st-1)
            else:
                if nums[st]+nums[en]>target:
                    en-=1
                if st<en:
                    if nums[en]+nums[st]<=target:
                        cnt+= 2**(en-st)
                elif st==en and nums[st]*2<=target:
                        cnt+=1
            cnt%=(10**9 + 7)
        return cnt
                    