class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        st = 0
        en = (rows-1)*cols+(cols-1)
        while st<=en:
            mid = (st+en)//2
            i, j = mid//cols,mid%cols
            val = matrix[i][j]
            if val == target:
                return True
            elif val>target:
                en = mid-1
            elif val<target:
                st = mid+1
        return False