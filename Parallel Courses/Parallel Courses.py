class Solution:
    def minimumSemesters(self, N: int, relations: List[List[int]]) -> int:
        # topological sort
        indeg = [0]*N
        adj = defaultdict(set)
        seen = set()
        
        for r in relations:
            adj[r[0]].add(r[1])
            indeg[r[1]-1] += 1
        # print(indeg)
        
        indeg_q = deque()
        for i,v in enumerate(indeg):
            if v==0: indeg_q.append(i+1)
        
        ans = 0
        while indeg_q:
            # print(indeg_q, seen, indeg)
            ans += 1
            length = len(indeg_q)
            for _ in range(length):
                node = indeg_q.popleft()
                seen.add(node)
                for n in adj[node]:
                    indeg[n-1] -= 1
                    if indeg[n-1]==0: indeg_q.append(n)
        
        # print(N)
        return ans if len(seen)==N else -1