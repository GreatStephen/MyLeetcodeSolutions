class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        edges = set()
        nodes = [0]*(n+1)
        for r in roads:
            edges.add(tuple(r))
            nodes[r[0]] += 1
            nodes[r[1]] += 1
        
        ans = 0
        for i in range(n):
            for j in range(i+1, n+1):
                tempans = nodes[i]+nodes[j]
                if (i,j) in edges or (j,i) in edges:
                    tempans -= 1
                ans = max(ans, tempans)
        
        return ans