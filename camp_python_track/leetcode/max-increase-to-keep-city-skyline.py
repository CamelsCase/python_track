class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        add = 0
        transpose = list(zip(*grid))
        rows = []
        cols = []
        for i in range(len(grid)):
                rows.append(max(grid[i]))
                cols.append(max(transpose[i]))
        for i in range(len(grid)):
            for j in range(len(grid)):
                val = min(rows[i],cols[j])-grid[i][j]
                add+=(val if val else 0)


        return add
        