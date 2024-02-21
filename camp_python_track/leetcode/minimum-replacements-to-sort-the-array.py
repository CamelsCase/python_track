class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        cnt = 0
        prev = nums[-1]
        for i in range(len(nums)-2,-1,-1):
            if prev<nums[i]:
                times = math.ceil(nums[i]/prev)
                prev = nums[i]//times
                cnt+=times-1
            else:
                prev = nums[i]
        return cnt


        