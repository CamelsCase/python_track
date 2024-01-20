class NumMatrix:

    def __init__(self, matrix: list[list[int]]):
        cols = len(matrix[0])
        rows = len(matrix)
        self.prefix = [[0 ]*(cols+1)  for j in range(rows+1)]
        self.matrix = matrix
        for col in range(cols):
            for row in range(rows):
                self.prefix[row+1][col+1] = self.prefix[row][col+1]+self.prefix[row+1][col]-self.prefix[row][col]+matrix[row][col]
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.prefix[row2+1][col2+1]-self.prefix[row1][col2+1]-self.prefix[row2+1][col1]+self.prefix[row1][col1]
        