class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # 二维dp，用减号，piles[i]-dp[i+1][j]，减号表示减去对方的max，即换了位
        # 如果dp[0][-1]大于0，说明自己比对方得分多
        N = len(piles)
        dp = [[0]*N for _ in range(N)]
        
        for l in range(1, N+1):
            for i in range(N-l+1):
                j = i+l-1
                dp[i][j] = max(piles[i]-(dp[i+1][j] if i+1<=j else 0), piles[j]-(dp[i][j-1] if i<=j-1 else 0))
        return dp[0][-1]>0