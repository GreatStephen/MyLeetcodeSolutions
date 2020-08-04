class Solution:
    def canCross(self, stones: List[int]) -> bool:
        # 用二维数组代替set
        N = len(stones)
        dp = [[False]*N for i in range(N)]
        dp[0][1] = True
        
        d = defaultdict(int)
        for i,s in enumerate(stones):
            d[s] = i
        
        
        for i,v in enumerate(stones):
            for step,flag in enumerate(dp[i]):
                if flag and v+step in d:
                    if v+step==stones[-1]:
                        return True
                    for newstep in (step-1, step, step+1):
                        if newstep<=0: continue
                        dp[d[v+step]][newstep] = True
        # print(dp)                         
        return False