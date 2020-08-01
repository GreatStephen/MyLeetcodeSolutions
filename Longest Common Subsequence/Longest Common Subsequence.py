class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # 二维dp数组，如果t1[i]==t2[i]，取左上角+1
        # 如果t1[i]!=t2[i]，取max（左，上）
        if len(text1)>len(text2):
            t = text1
            text1 = text2
            text2 = t
        R, C = len(text1), len(text2)
        dp = [[0]*C for _ in range(R)]
        for i in range(R):
            for j in range(C):
                if text1[i]==text2[j]: 
                    dp[i][j] = (dp[i-1][j-1] if i>0 and j>0 else 0) +1
                else:
                    dp[i][j] = max((dp[i-1][j] if i>0 else 0), (dp[i][j-1] if j>0 else 0))
        return dp[-1][-1]