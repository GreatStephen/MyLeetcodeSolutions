class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        # 滑窗+DP，滑窗大小=W，滑窗内所有概率之和除以W，即为dp[i]的概率
        # 但滑窗r边界不允许>=K，注意滑窗的shrink当到达最右侧
        if N>=K-1+W or K==0: return 1.0
        dp = [1.0] + [0.0]*N
        l,r, wsum = 0,0, 1.0
        for p in range(1, N+1):
            if p>K-1+W: break
            dp[p] = wsum/W
            r = p
            if r<K:
                wsum+=dp[r]
            if r-l+1>W:
                wsum-=dp[l]
                l+=1
        return sum(dp[K:])