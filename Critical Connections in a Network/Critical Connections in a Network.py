class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        d = collections.defaultdict(set)
        seen = collections.defaultdict(list)    # node: [disc, low]
        for s,t in connections:
            d[s].add(t)
            d[t].add(s)
        
        ans = []
        def DFS(node, dis):
            disc = low = dis
            seen[node] = [disc, low]
            next_edges = set(d[node])
            for next in next_edges:
                if next not in d[node]: continue
                d[node].discard(next)
                d[next].discard(node)
                if next not in seen:
                    v = DFS(next, dis+1)
                    if v[1]>disc:
                        # this is a critical edge
                        ans.append([node, next])
                    else:
                        # updage the low
                        low = min(low, v[1])
                else:
                    # find a cycle
                    low = min(low, seen[next][1])
                    seen[node] = [disc, low]
            return (disc, low)
        
        DFS(0,0)
        return ans