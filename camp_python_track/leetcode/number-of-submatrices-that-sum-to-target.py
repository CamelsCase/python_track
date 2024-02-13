class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        pre2d = [[0]*(cols+1) for _ in range(rows+1)]
        for i in range(rows):
            for j in range(cols):
                pre2d[i+1][j+1] = pre2d[i][j+1]+pre2d[i+1][j]-pre2d[i][j]+matrix[i][j]

        cnt = 0        
        for r1 in range(rows):
            for r2 in range(r1,rows):
                dt = {0:1}
                for c in range(cols):
                    if pre2d[r2+1][c+1]-pre2d[r1][c+1]-target in dt:
                        cnt+=dt[pre2d[r2+1][c+1]-pre2d[r1][c+1]-target]
                    if not pre2d[r2+1][c+1]-pre2d[r1][c+1] in dt:
                        dt[pre2d[r2+1][c+1]-pre2d[r1][c+1]] = 1
                    else:
                        dt[pre2d[r2+1][c+1]-pre2d[r1][c+1]]+=1
                
        return cnt