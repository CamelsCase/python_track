class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        def backtrack(st,candidate):
            if len(candidate)==k:
                result.append(candidate.copy())
                return
            for i in range(st,n+1):
                candidate.append(i)
                backtrack(i+1,candidate)
                candidate.pop()
        backtrack(1,[])
        return result
                