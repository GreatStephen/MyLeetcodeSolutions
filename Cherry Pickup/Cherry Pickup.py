class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        # bottom up, dp[][][]
        N = len(grid)
        dp = [[[0]*N for __ in range(N)] for _ in range(2*N-1)]
        # print(len(dp[0][0]))
        
        for n in range(2*N-2, -1, -1):
            for i in range(N):
                for p in range(N):                    
                    if 0<=i<N and 0<=n-i<N and 0<=p<N and 0<=n-p<N:
                        if grid[i][n-i]==-1 or grid[p][n-p]==-1: continue
                        if n==2*N-2:
                            dp[n][N-1][N-1] = grid[N-1][N-1]
                            continue
                        # print(n, i, p)
                        temp = grid[i][n-i] if (i,n-i)==(p,n-p) else grid[i][n-i] + grid[p][n-p]
                        next_move = -1
                        
                        # i, p right
                        if 0<=n-i+1<N and 0<=n-p+1<N and grid[i][n-i+1]!=-1 and grid[p][n-p+1]!=-1:
                            next_move = max(next_move, dp[n+1][i][p])
                        # i, p down
                        if 0<=i+1<N and 0<=p+1<N and grid[i+1][n-i]!=-1 and grid[p+1][n-p]!=-1:
                            next_move = max(next_move, dp[n+1][i+1][p+1])
                        # i right, p down
                        if 0<=n-i+1<N and 0<=p+1<N and grid[i][n-i+1]!=-1 and grid[p+1][n-p]!=-1:
                            next_move = max(next_move, dp[n+1][i][p+1]) 
                        #i down, p right
                        if 0<=i+1<N and 0<=n-p+1<N and grid[i+1][n-i]!=-1 and grid[p][n-p+1]!=-1:
                            next_move = max(next_move, dp[n+1][i+1][p]) 
                        dp[n][i][p] = -1 if next_move==-1 else (temp+next_move)
                        # print(dp[n][i][p])
               
        # print(dp)
        return max(dp[0][0][0], 0)