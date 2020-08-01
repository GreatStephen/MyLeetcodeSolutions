class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        # 跟house robber 2很像，也是收尾相连，选择[0:-2]和[1:-1]的最大值
        # 已经选了几个数 n，作为附加信息，三维dp
        N = len(slices)
        dp = [[[0]*(N+1) for i in range(N)] for j in range(N)]
        
        def helper(i, j, n):
            if j-i+1<2*n-1: return 0
            if dp[i][j][n]!=0: return dp[i][j][n]
            if n==1: 
                ans = max(slices[i:j+1])
                dp[i][j][n] = ans
                return ans
            
            
            ans = max(helper(i,j-2, n-1)+slices[j], helper(i,j-1,n))
            dp[i][j][n] = ans
            return ans
        
        
        
        return max(helper(0, N-2, N//3), helper(1, N-1, N//3))