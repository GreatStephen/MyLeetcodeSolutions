class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # 如果s[i]=s[j]，说明两头相等，中间的最大值可以+2
        # 如果s[i]!=s[j]，说明两头不等，只能取一个，[i+1]到[j]和[i]到[j-1]之中取最大值
        dp = [[0]*len(s) for j in range(len(s))]
        for i in range(len(s)): dp[i][i] = 1
        # print(dp)
        
        for length in range(1,len(s)):
            for i in range(len(s)-length):
                j = i+length
                if s[i]==s[j]: dp[i][j] = dp[i+1][j-1]+2
                else: dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return dp[0][-1]