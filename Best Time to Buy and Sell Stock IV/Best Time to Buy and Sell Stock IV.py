class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices: return 0
        if k>(len(prices)//2): # 防止k过大的情况
            ans = 0
            for i in range(1, len(prices)):
                ans += max(0, prices[i]-prices[i-1])
            return ans
            
        dp = [[0]*len(prices) for i in range(k+1)]
        
        for i in range(1, k+1):
            tempmax = 0 - prices[0] # 优化，随循环记录最大的tempmax, tempmax+cur=当前的最大值
            profit = 0
            for j in range(1, len(prices)):
                profit = max(profit, prices[j]+tempmax)
                tempmax = max(tempmax, (dp[i-1][j-1] if j>0 else 0)-prices[j])
                dp[i][j] = profit
        
        
        # print(dp)
        return dp[-1][-1]