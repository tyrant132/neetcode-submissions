class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        memo = [[0]*n for i in range(m)]
        memo[0][0] = grid[0][0]
        for _ in range(1,n):
            memo[0][_] = memo[0][_-1]+grid[0][_]
        for _ in range(1,m):
            memo[_][0] = memo[_-1][0]+grid[_][0]
        for i in range(1,m):
            for j in range(1,n):
                memo[i][j] = grid[i][j]+min(memo[i-1][j],memo[i][j-1])
        return memo[m-1][n-1]
        