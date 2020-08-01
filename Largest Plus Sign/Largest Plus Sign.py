class Solution:
    def orderOfLargestPlusSign(self, N: int, mines: List[List[int]]) -> int:
        # 用dp分别记录四个方向的延伸长度，取最小值，最后取整个dp的最大值
        dp = [[N]*N for _ in range(N)]
        matrix = [[1]*N for _ in range(N)]
        for x,y in mines: matrix[x][y]=0       
        def helper(count, matrix, dp, i, j):
            if matrix[i][j]==0: count = 0
            else: count += 1
            dp[i][j] = min(dp[i][j], count)  
            return count    
        for i in range(N):
            #left
            count = 0
            for j in range(N): count = helper(count, matrix, dp, i, j)
            #right
            count = 0
            for j in range(N-1,-1,-1): count = helper(count, matrix, dp, i, j)                
        for j in range(N):
            #up
            count = 0
            for i in range(N): count = helper(count, matrix, dp, i, j)
            #down
            count = 0
            for i in range(N-1, -1, -1): count = helper(count, matrix, dp, i, j)        
        return max([max(row) for row in dp])
            