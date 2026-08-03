class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if obstacleGrid[0][0]==1 or obstacleGrid[m-1][n-1]==1:
            return 0
        memo = [[0]*n for i in range(m)]
        for _ in range(n):
            if obstacleGrid[0][_]==1:
                break
            memo[0][_] = 1
        for _ in range(m):
            if obstacleGrid[_][0]==1:
                break
            memo[_][0] = 1
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j]==1:
                    memo[i][j] = 0
                else:
                    memo[i][j] = memo[i-1][j]+memo[i][j-1]
        return memo[m-1][n-1]
        