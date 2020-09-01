class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # 常规的DFS遍历。如果cur没有指向DFS，就计数+1即可
        nextnodes, adj = {}, {}
        for c in connections:
            if c[0] not in adj:
                adj[c[0]] = set()
            if c[1] not in adj:
                adj[c[1]] = set()
            adj[c[0]].add(c[1])
            adj[c[1]].add(c[0])
            if c[0] not in nextnodes:
                nextnodes[c[0]] = set()
            nextnodes[c[0]].add(c[1])
        
        self.ans = 0
        seen = set()
        def DFS(cur, parent):
            if parent!=None:
                if cur not in nextnodes or parent not in nextnodes[cur]:
                    self.ans += 1
            for n in adj[cur]:
                if n in seen:
                    continue
                seen.add(n)
                DFS(n, cur)
                
        seen.add(0)
        DFS(0, None)
        return self.ans