class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        leng = len(nums)
        def backtrack(st,path):
            if not st:
                ans.append(path[:])
                return 
            for i in range(0,len(st)):
                path.append(st[i])
                backtrack(st[:i] + st[i + 1:], path)
                path.pop()

        backtrack(nums[:],[])
        return ans
                
