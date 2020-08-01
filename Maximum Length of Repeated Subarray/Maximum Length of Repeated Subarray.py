class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        # dp[i][j]是以A[i]&B[j]结尾的最长子串
        # 如果A[i]!=B[j]，dp直接=0
        # 在LCS问题中，如果A[i]!=B[j]，dp=前面的最大值
        R, C = len(A), len(B)
        dp = [[0]*C for i in range(R)]
        
        ans = 0
        for i in range(R):
            for j in range(C):
                if A[i]==B[j]:
                    dp[i][j] = (dp[i-1][j-1] if i>0 and j>0 else 0) + 1
                    ans = max(ans, dp[i][j])
                else:
                    dp[i][j] = 0
        return ans