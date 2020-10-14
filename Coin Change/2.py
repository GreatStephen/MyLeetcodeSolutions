class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 这是一个暴力解法，虽然用了dp，但实际复杂度还是一棵N叉树
        dp = [float('inf')]*(amount+1)
        dp[0] = 0

        def helper(n):
            if n<0:
                return -1
            if not dp[n]==float('inf'):
                return dp[n]
            ans = float('inf')
            for c in coins:
                temp = helper(n-c)
                if temp>=0:
                    ans = min(ans, temp+1)
            
            dp[n] = ans if not ans==float('inf') else -1
            return dp[n]


        helper(amount)
        return dp[amount]