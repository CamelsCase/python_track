class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        leng = len(nums)
        def backtrack(st,path):
            for i in range(st,leng):
                path.append(nums[i])
                x = sorted(path)
                if not x in ans:
                    ans.append(x)
                backtrack(i+1,path)
                path.pop()
        backtrack(0,[])
        return ans
                
