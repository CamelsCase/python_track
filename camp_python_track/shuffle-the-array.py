class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        out = []
        for  i in range(n):
            out.append(nums[:n][i])
            out.append(nums[n:][i])
        return out