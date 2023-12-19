class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        leng = len(matrix[0])
        prev = matrix[0][0]
        for j in range(1,len(matrix)):
            for i in range(1,leng):
                if matrix[j][i]!=matrix[j-1][i-1]:
                    return False
        return True