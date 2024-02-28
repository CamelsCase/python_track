class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mp = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        ans = []
        leng = len(digits)
        def backtrack(ind,path):
            if len(path)==leng and leng!=0:
                ans.append("".join(path[:]))
            if ind>=leng:
                return
            for ch in mp[digits[ind]]:
                path.append(ch)
                backtrack(ind+1,path)
                path.pop()
        backtrack(0,[])
        return ans
