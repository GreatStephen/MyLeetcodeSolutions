class Solution:
    def minRefuelStops(self, target, cur, s):
        # greedy，把当前distance能到达的站的油量heap，永远取能给我最多油的站。
        # 如果这个站的油还不能到终点，再更新能到达的站，再取最多油
        # 直到到站为止
        pq = []
        res = i = 0
        while cur < target:
            while i < len(s) and s[i][0] <= cur:
                heapq.heappush(pq, -s[i][1])
                i += 1
            if not pq: return -1
            cur += -heapq.heappop(pq)
            res += 1
        return res