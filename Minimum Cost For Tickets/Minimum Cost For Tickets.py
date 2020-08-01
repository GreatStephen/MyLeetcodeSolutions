class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        offset = {0:1, 1:7, 2:30}
        dp = [[0]*len(days) for _ in range(3)]
        
        for i in range(3):
            for j in range(len(days)):
                ans = 10**9
                for k in range(i, -1, -1):
                    pos = bisect.bisect(days, days[j]-offset[k])
                    cost = (dp[i][pos-1] if pos>0 else 0) + costs[k]
                    ans = min(ans, cost)
                dp[i][j] = ans
        
        
        # print(dp)
        return dp[-1][-1]