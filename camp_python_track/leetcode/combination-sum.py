class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        leng = len(candidates)
        def backtrack(index,path,sm):
            # print(index,path,sm)
            if sm==target:
                if path not in ans:
                    ans.append(path[:])
            if target<sm:
                return
            if index>=leng:
                return
            for i in range(index,leng):
                path.append(candidates[i])
                sm+=candidates[i]
                backtrack(i,path,sm)
                sm-=path.pop()
        for i in range(leng):
            backtrack(i,[],0)
        return ans
