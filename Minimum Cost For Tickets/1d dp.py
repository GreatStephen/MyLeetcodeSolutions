class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        offset = {0:1, 1:7, 2:30}
        dp = []
        
        for i in range(len(days)):
            ans = 10**9
            for k in range(3):
                pos = bisect.bisect(days, days[i]-offset[k])
                cost = (dp[pos-1] if pos>0 else 0) + costs[k]
                ans = min(ans, cost)
            dp.append(ans)
        return dp[-1]