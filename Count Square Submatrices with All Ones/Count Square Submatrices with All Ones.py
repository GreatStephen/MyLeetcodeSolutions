class Solution:
    def countSquares(self, M: List[List[int]]) -> int:
        R,C = len(M), len(M[0])
        dp = [[0]*C for _ in range(R)]
        
        for i in range(R):
            count = 0
            for j in range(C-1, -1, -1):
                if M[i][j]==1: count+=1
                else: count=0
                dp[i][j] = count
        
        # print(dp)
        ans = 0
        for i in range(R):
            for j in range(C):
                minval=dp[i][j]
                for k in range(dp[i][j]):
                    if i+k >= R: break
                    if dp[i+k][j]>=k+1 and k+1<=minval: 
                        ans += 1
                        minval = min(minval, dp[i+k][j])
                    else: break
        
        return ans