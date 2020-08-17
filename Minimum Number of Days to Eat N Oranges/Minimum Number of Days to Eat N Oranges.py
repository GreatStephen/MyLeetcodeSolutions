class Solution(object):
    def minDays(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 用map代替dp数组，会变快
        d = {}
        def dp(n):
            if n<=1:
                return 1
            if n in d:
                return d[n]
            ans = float('inf')
            ans = min(ans, n%3+dp(n/3)+1)
            ans = min(ans, n%2+dp(n/2)+1)
            d[n] = ans
            return ans
        
        return dp(n)