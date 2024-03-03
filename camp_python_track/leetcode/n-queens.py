class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        path = []
        ans = []
        attackable_row = set()
        up_diagonal = set()
        down_diagonal = set()
        def find(row,col,rem):
            nonlocal path
            nonlocal attackable_row        
            nonlocal up_diagonal
            nonlocal down_diagonal
            if len(path)==n and rem==0:
                found = path[:]
                if not found in ans:
                    ans.append(found)
                return 
            for r in range(n):
                if not r in attackable_row:
                    if not r+col in up_diagonal and  not r-col in down_diagonal:
                        x = ["."]*n
                        x[r] ="Q"
                        path.append("".join(x))
                        attackable_row.add(r)
                        up_diagonal.add(r+col)
                        down_diagonal.add(r-col)
                        find(r,col+1,rem-1)
                        path.pop()
                        attackable_row.remove(r)
                        up_diagonal.remove(r+col)
                        down_diagonal.remove(r-col)
        find(0,0,n)
        return ans



