class Solution:
    def countSquares(self, M: List[List[int]]) -> int:
        # Lee的方法更好
        # dp[i][j]=min(左边，上边，左上)+1
        R,C = len(M), len(M[0])
        dp = [[0]*(C+1) for _ in range(R+1)]
        
        ans = 0
        for i in range(1, R+1):
            for j in range(1, C+1):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])+1 if M[i-1][j-1]==1 else 0
                ans += dp[i][j]
        return ans