class Solution(object):
    def checkRecord(self, n):
        """
        :type n: int
        :rtype: int
        """

        # 独立做出来的hard DP, O(N)
        # 第一行代表以A结尾，第二行代表以L结尾，第三行代表以P结尾，第四行代表以L结尾但不含A，第五行代表以P结尾但不含A
        # 第四第五行是因为，以A结尾需要他俩之和
        # A = LwoA[i-1] + PwoA[i-1]
        # L = (A+L+P)[i-1] - (A+P)[i-3]减去末尾三个都是L但倒数第四位不是L的情况
        # P = (A+L+P)[i-1]
        # LwoA = (LwoA+PwoA)[i-1] - PwoA[i-3]同样减去倒数第四位不是L的情况
        # PwoA = (LwoA+PwoA)[i-1]
        # 最后结果是A+L+P
        MOD = 10**9+7
        dp = [[0]*(n+1) for _ in xrange(5)]
        for i in xrange(5):
            dp[i][1] = 1
        
        for j in xrange(2, n+1):
            A = dp[3][j-1]+dp[4][j-1]
            dp[0][j] = A%MOD
            
            L = dp[0][j-1]+dp[1][j-1]+dp[2][j-1]
            if j==3: L-=1
            elif j>3: L-=(dp[0][j-3]+dp[2][j-3])
            dp[1][j] = L%MOD
            
            P = dp[0][j-1]+dp[1][j-1]+dp[2][j-1]
            dp[2][j] = P%MOD
            
            LwoA = dp[3][j-1]+dp[4][j-1]
            if j==3: LwoA -= 1
            elif j>3: LwoA -= dp[4][j-3]
            dp[3][j] = LwoA%MOD
            
            PwoA = dp[3][j-1]+dp[4][j-1]
            dp[4][j] = PwoA%MOD
        
        
        return (dp[0][-1]+dp[1][-1]+dp[2][-1])%MOD