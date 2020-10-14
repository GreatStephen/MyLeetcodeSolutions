class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 比tree暴力解更快，bottom up，从0搭建dp数组。O(len(coin)*amount)
        dp = [float('inf')] * (amount+1)
        dp[0] = 0
        
        for i in range(1, amount+1):            
            for c in coins:
                if i-c>=0:
                    dp[i] = min(dp[i], dp[i-c]+1)
        
        return dp[-1] if dp[-1]<float('inf') else -1