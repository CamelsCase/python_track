class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        leng = len(nums)
        prefix = [0]*(leng+1)
        out = []
        for i in range(len(nums)):
            prefix[i+1] = nums[i]+prefix[i]
        for i in range(leng):
            out.append(nums[i]*(i)-prefix[i]+ prefix[leng]-prefix[i+1]-nums[i]*(leng-1-i))
        return out