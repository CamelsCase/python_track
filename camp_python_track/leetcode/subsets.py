class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        def backtrack(st,candidate):
            for i in range(st,len(nums)):
                candidate.append(nums[i])
                result.append(candidate.copy())
                backtrack(i+1,candidate)
                candidate.pop()
        backtrack(0,[])
        return result