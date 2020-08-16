class Solution(object):
    def minDays(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        dp = [0,1]+[0]*(n-1)
        
        for i in range(2, n+1):
            ans = i
            ans = min(ans, dp[i-1]+1)
            if not i%3:
                ans = min(ans, dp[i/3]+1)
            if not i&1:
                ans = min(ans, dp[i/2]+1)
            dp[i] = ans
        
        return dp[-1]

# 9459568
15 5
20 5
30 5
100 8
346 10
567 8
1234 12
[0, 1, 2, 2, 3, 4, 3, 4, 4, 3, 4, 5, 4, 5, 5, 5, 5, 6, 4, 5, 5, 5, 6, 7, 5, 6, 6, 4, 5, 6, $$5, 6, 6, 6, 7, 8, 5, 6, 6, 6, $$6, 7, 6, 7, 7, 6, 7, 8, 6, 7, 7]

84806671 32
2826890 24
42403335