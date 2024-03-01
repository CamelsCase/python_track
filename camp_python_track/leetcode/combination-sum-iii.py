class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        candidates = [i+1 for i in range(min(n,9))]
        if 9*k<n:
            return []
        ans = []
        def all_valids(index,path,target):
            if len(path)==k and target==0:
                ans.append(path[:])
                return 
            elif n<0:
                return 
            for i in range(index,9+1):
                if len(path)<k:
                    path.append(i)
                    all_valids(i+1,path,target-i)
                    path.pop()
        all_valids(1,[],n)
        return ans
            
