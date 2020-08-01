class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        d = collections.defaultdict(set)
        seen = set()
        self.ans = [-1]*n
        
        for e in edges:
            d[e[0]].add(e[1])
            d[e[1]].add(e[0])
        # print(d)
        
        def DFS(node):
            ansd = collections.defaultdict(int)
            ansd[labels[node]] = 1
            seen.add(node)
            for next in d[node]:
                if next not in seen:
                    # seen.add(next)
                    next_d = DFS(next)
                    # if node==0: print(next_d)
                    for k,v in next_d.items():
                        ansd[k]+=v
            self.ans[node] = ansd[labels[node]]
            return ansd
        
        DFS(0)
        return self.ans