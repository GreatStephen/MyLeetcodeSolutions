class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        hp = []
        heapq.heapify(hp)
        
        for i in range(N):
            for j in range(i+1, N):
                heapq.heappush(hp, (abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1]), i, j))
        # print(hp[0])
        
        group = [i for i in range(N)]
        def find(x):
            if x==group[x]: return x
            group[x] = find(group[x])
            return group[x]
        
        ans = 0
        while hp:
            edge, n1, n2 = heapq.heappop(hp)
            g1, g2 = find(n1), find(n2)
            if g1!=g2:
                ans += edge
                group[g1] = g2
        return ans