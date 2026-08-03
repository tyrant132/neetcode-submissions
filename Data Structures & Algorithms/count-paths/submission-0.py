class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[0]*n for i in range(m)]
        for _ in range(n):
            memo[0][_] = 1
        for _ in range(m):
            memo[_][0] = 1
        for i in range(1,m):
            for j in range(1,n):
                memo[i][j] = memo[i-1][j]+memo[i][j-1]
        return memo[m-1][n-1]