class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        
        newmat = [[-10**9-1 for  i in range(len(matrix))]for  i in range(len(matrix[0]))]
        for col in range(len(matrix[0])):
            for row in range(len(matrix)):
                newmat[col][row] = matrix[row][col]
        return newmat