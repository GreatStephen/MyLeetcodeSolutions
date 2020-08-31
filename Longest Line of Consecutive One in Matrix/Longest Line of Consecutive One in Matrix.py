class Solution:
    def longestLine(self, M: List[List[int]]) -> int:
        # 简单的dp题，对[i,j]存放一个tuple，[右侧长度，下方长度，右下长度，左下长度]
        if not M or not M[0]:
            return 0
        R,C = len(M), len(M[0])
        dp = [[None]*C for _ in range(R)]
        self.ans = 0
        
        def helper(r,c):
            if not 0<=r<R or not 0<=c<C or not M[r][c]:
                return (0,0,0,0)
            if dp[r][c]:
                return dp[r][c]
            right, bottom, br,bl = helper(r,c+1), helper(r+1,c), helper(r+1, c+1), helper(r+1, c-1)
            
            # 可以肯定的是当前grid的数字是1. 对于四个方向，把它们的长度都加1
            cur = (right[0]+1, bottom[1]+1, br[2]+1, bl[3]+1)
            # 再更新一下最长长度
            self.ans = max(self.ans, max(cur))
            dp[r][c] = cur
            return cur
        
        for i in range(R):
            for j in range(C):
                if M[i][j]: helper(i,j)
        return self.ans