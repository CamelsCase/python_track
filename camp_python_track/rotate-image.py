class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        mx = []
        leng = len(matrix)
        for col in range(leng):
            o = []
            for row in range(leng):
                o.append(matrix[row][col])
            mx.append(o[::-1])
        ind = 0
        for i in mx:
            matrix[ind] =i
            ind+=1 
      