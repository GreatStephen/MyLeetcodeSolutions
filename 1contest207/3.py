class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        R,C = len(grid), len(grid[0])
        dp = [[None]*C for _ in range(R)] # dp[i,j] = [+max, -max]
        self.MOD = 10**9+7
        self.has_zero = False
        
        def DP(r,c):
            if r<R and c<C and grid[r][c]==0:
                dp[r][c] = [0,0]
                self.has_zero = True
                return dp[r][c]
            if r==R-1 and c==C-1:
                if grid[r][c]==0:  ans = [0,0]
                elif grid[r][c]>0: ans = [grid[r][c], 0]
                elif grid[r][c]<0:  ans = [0, grid[r][c]]
                dp[r][c] = ans
                return dp[r][c]
            if r>=R or c>=C:
                return [0,0]
            if dp[r][c]!=None:
                return dp[r][c]
            pos, neg = 0, 0          
            if grid[r][c]>0:
                val = DP(r,c+1)
                pos = max(pos, grid[r][c]*val[0])
                neg = min(neg, grid[r][c]*val[1])
                val = DP(r+1,c)
                pos = max(pos, grid[r][c]*val[0])
                neg = min(neg, grid[r][c]*val[1])
            elif grid[r][c]<0:
                val = DP(r,c+1)
                # print(r,c,val)
                pos = max(pos, grid[r][c]*val[1])
                neg = min(neg, grid[r][c]*val[0])
                val = DP(r+1,c)
                # print(r,c,val)
                pos = max(pos, grid[r][c]*val[1])
                neg = min(neg, grid[r][c]*val[0])
            # print(ans)
            dp[r][c] = [pos, neg]
            return dp[r][c]
                
        
        
        DP(0,0)
        # print(self.has_zero)
        # print(dp[5][4])
        return dp[0][0][0]%self.MOD if self.has_zero or dp[0][0][0]%self.MOD>0 else -1