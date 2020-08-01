class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        d = collections.defaultdict(dict)
        for (s1,s2),v in zip(equations, values):
            d[s1][s2] = v
            d[s2][s1] = 1/v

        self.seen = set()
        def DFS(start, end, temp_res):
            if start==end and start in d: return temp_res
            for (next, val) in d[start].items():
                if next not in self.seen: 
                    self.seen.add(next)
                    res = DFS(next, end, temp_res*val)
                    self.seen.remove(next)
                    if res!='*': return res
            return '*'
        
        ans = []
        for (start, end) in queries:
            self.seen.clear()
            res = DFS(start, end, 1)
            if res!='*':
                d[start][end] = res
                d[end][start] = 1/res
                ans.append(res)
            else: ans.append(-1)
        
        return ans