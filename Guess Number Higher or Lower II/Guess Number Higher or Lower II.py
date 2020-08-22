class Solution(object):
    def getMoneyAmount(self, n):
        dp = [[-1]*(n+1) for i in range(n+1)]
        
        def DP(x, y):
            if x>=y:
                return 0
            if dp[x][y] != -1:
                return dp[x][y]
            ans = float('inf')
            for i in range(x, y+1):
                temp = i + max(DP(x,i-1), DP(i+1,y))
                ans = min(ans, temp)
            dp[x][y] = ans
            return ans
        
        
        return DP(1,n)
        