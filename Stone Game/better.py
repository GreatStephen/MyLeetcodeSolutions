class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # 一维dp，dp[i]代表[i:i+l-1]
        N = len(piles)
        dp = piles[:]
        for l in range(2, N+1):
            for i in range(N-l+1):
                dp[i] = max(piles[i]-dp[i+1], piles[i+l-1]-dp[i])
        return dp[0]>0