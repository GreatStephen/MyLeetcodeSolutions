class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        dp = []
        maxd = deque()
        l, r = 0, 0
        MAX = -(10**4+1)
        
        for n in nums:
            dp.append(n+max(0, (maxd or [0])[0]))
            MAX = max(MAX, dp[-1])
            while maxd and maxd[-1]<dp[-1]:
                maxd.pop()
            maxd.append(dp[-1])
            r+=1
            if r-l>k:
                if maxd[0]==dp[l]: maxd.popleft()
                l+=1
        
        return MAX