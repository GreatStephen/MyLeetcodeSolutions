class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # 比较简单的dp，dp[i][j]检查s1[:i]和s2[:j]能否组成s3[:i+j]
        if len(s1)+len(s2)!=len(s3): return False
        R,C = len(s1), len(s2)
        dp = [[False]*(C+1) for i in range(R+1)]
        dp[0][0] = True
        
        for i in range(R):
            if s1[i]==s3[i] and dp[i][0]:
                dp[i+1][0] = True
        for j in range(C):
            if s2[j]==s3[j] and dp[0][j]:
                dp[0][j+1] = True
        
        for i in range(1, R+1):
            for j in range(1, C+1):
                if not dp[i-1][j] and not dp[i][j-1]:
                    continue
                if dp[i][j-1] and s2[j-1]==s3[i+j-1]: # 当前字符与s2相等，检查左边==True
                    dp[i][j] = True
                elif dp[i-1][j] and s1[i-1]==s3[i+j-1]: # 当前字符与s1相等，检查上边==True
                    dp[i][j] = True
        
        return dp[-1][-1]