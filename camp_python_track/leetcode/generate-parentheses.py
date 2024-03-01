class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        ans  = []
        def backtrack(_open,_close,path):
            if _open==_close:
                if len(path)==2*n:
                    # print(path)
                    ans.append("".join(path))
                else:
                    #you must choose opening,(
                    path.append("(")
                    _open+=1
            elif _open==n:
                #you must consider only the closing brace,)
                remaining = n-_close
                for j in range(remaining):
                    path.append(")")
                    _close+=remaining
                ans.append("".join(path))
                
            if _open<n:
                backtrack(_open+1,_close,path[:]+["("])
            if _open>_close:
                backtrack(_open,_close+1,path[:]+[")"])
        backtrack(0,0,[])
        return ans
            
            
            