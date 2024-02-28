# A   B   C   E
# S   F   C   S
# A   D   E   E

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        leng = len(word)
        row_length = len(board)
        col_length = len(board[0])
        rec_func = [(0,1),(0,-1),(1,0),(-1,0)]
        def backtrack(row,col,index,path):
            #this is the base case
            if len(path)>=leng or index==leng:
                return True
            if not (0<=row<row_length and 0<=col<col_length):
                return
            if board[row][col]!=word[index]:
                return 
            if (row,col) in path:
                return
            path.append((row,col))
            for i in rec_func:
                ans = backtrack(row+i[0],col+i[1],index+1,path)
                if ans:
                    return True
            path.pop()
        for r in range(row_length):
            for c in range(col_length):
                ans = backtrack(r,c,0,[])
                if ans:
                    return ans
        return False