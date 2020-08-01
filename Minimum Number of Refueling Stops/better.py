class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        # N^2 DP，dp[t]=t次加油的最长距离，dp[t]和stations[i]要同时循环
        # 对dp[t]，找t-1之前的所有距离大于station[i]的，然后更新dp[t]为那个站的最长距离加上加油距离，取最大
        dp = [startFuel]+[0]*len(stations)
        for i in range(len(stations)):
            for t in range(i+1, 0, -1):
                if dp[t-1]>=stations[i][0]:
                    dp[t] = max(dp[t], dp[t-1]+stations[i][1])
                else: break
        # print(dp)
        for i in range(len(dp)):
            if dp[i]>=target: return i
        return -1