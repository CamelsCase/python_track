class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        right = sum(nums)
        left = 0
        dt = Counter()
        dt[0] =right
        for i in range(len(nums)):
            if nums[i]==0:
                left+=1
            else:
                right-=1
            dt[i+1] = left+right
        mx= dt.most_common()[0][1]
        return [i[0] for i in dt.items() if i[1]==mx]