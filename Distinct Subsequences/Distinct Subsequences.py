class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # 二维dp，如果当前字符相等，分两种情况，包括当前字符（左边）+不包括当前字符（左上角）
        # 如果当前字符不等，则只取左边
        dp = [[0]*(len(s)+1) for _ in range(len(t)+1)] 
        for j in range(len(s)+1): dp[0][j] = 1
        
        for i in range(1, len(t)+1):
            for j in range(1, len(s)+1):
                if s[j-1]!=t[i-1]: dp[i][j] = dp[i][j-1]
                else: dp[i][j] = dp[i-1][j-1]+dp[i][j-1]
        
        return dp[-1][-1]