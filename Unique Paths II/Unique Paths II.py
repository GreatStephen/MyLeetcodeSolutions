class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        R, C = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0]*(C+1) for _ in range(R+1)]
        dp[R-1][C-1] = 1
        
        for i in range(R-1, -1, -1):
            for j in range(C-1, -1, -1):
                if obstacleGrid[i][j]==1: dp[i][j] = 0
                else: 
                    if i==R-1 and j==C-1: continue
                    dp[i][j] = dp[i+1][j] + dp[i][j+1]
        
        
        return dp[0][0]