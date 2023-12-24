class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #check row
        for i in board:
            seen = set()
            for j in i:
                if j.isdigit() and j not in seen:
                    seen.add(j)
                elif j in seen:
                    print("found ",j)
                    return False
        #check col
        for i in range(9):
            seen = set()
            for j in range(9):
                if board[j][i].isdigit() and board[j][i] not in seen:
                    seen.add(board[j][i])
                elif board[j][i] in seen:
                    print("found at",board[j][i])
                    return False
        #check cell
        for i in range(0,9,3):
            for j in range(0,9,3):
                seen = set()
                for row in range(i,i+3):
                    for col in range(j,j+3):
                        x = board[row][col]
                        if x.isdigit() and  x not in seen:
                            seen.add(x)
                        elif x in seen:
                            # print("cell",i,j,board[row][col])
                            return False      
        return True
        