class Solution:
    def sortColors(self, nums: List[int]) -> None:
        freq = Counter(nums)
        ind = 0
        for i in {0,1,2}:
            for fr in range(freq[i]):
                nums[ind] = i
                ind+=1