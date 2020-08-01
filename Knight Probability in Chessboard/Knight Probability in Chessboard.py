class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        dp =[[0.0]*N for _ in range(N)]
        dp[r][c] = 1.0
        moves = [(-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1)]
        
        for k in range(K):
            tempdp = [[0.0]*N for _ in range(N)]
            for i in range(N):
                for j in range(N):
                    for m in moves:
                        newi, newj = i+m[0], j+m[1]
                        if 0<=newi<N and 0<=newj<N and dp[newi][newj]!=0:
                            tempdp[i][j] += dp[newi][newj] * 0.125
            dp = tempdp
        
        return sum([sum(row) for row in dp])