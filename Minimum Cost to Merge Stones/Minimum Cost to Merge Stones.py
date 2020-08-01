class Solution:
    def mergeStones(self, stones: List[int], K: int) -> int:
        # 三维dp数组，第三维是最终结果=k堆，先算dp[][][2]->dp[][][K]，
        # 最后合并成一个堆dp[][][1] = sum(stones) + dp[][][K]
        N= len(stones)
        dp =[[[10**9]*(K+1) for i in range(N+1)] for j in range(N+1)]
        
        for i in range(N+1):
            dp[i][i][1] = 0
        
        for l in range(2, N+1):
            for i in range(1, N+2-l):
                j = i+l-1
                summ = sum(stones[i-1:j])
                for k in range(2, K+1):
                    temp_res = 10**9
                    for div in range(i, j):
                        temp_res = min(temp_res, dp[i][div][1]+dp[div+1][j][k-1])
                    dp[i][j][k] = temp_res
                dp[i][j][1] = summ + dp[i][j][k]
        
        return dp[1][-1][1] if dp[1][-1][1]<10**9 else -1