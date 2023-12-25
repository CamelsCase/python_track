class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        leng = len(mat)
        sm = 0
        for i in range(leng):
            sm+=mat[i][i]+mat[i][leng-i-1]
        return sm if leng%2==0 else sm-mat[leng//2][leng//2]

        