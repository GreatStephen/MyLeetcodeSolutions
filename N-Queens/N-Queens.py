class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if not n: return [[]]
        ans = []
        def build(path):
            a, s = [], ''
            for _ in range(n): s+='.'
            for p in path:                
                a.append(s[:p]+'Q'+s[p+1:])
            ans.append(a)            
        # oc = [{row},{col},{dia},{antidia}]
        def DFS(r, c, oc, path):
            path.append(c)
            if r==n-1: 
                build(path)  
                return
            oc[0].add(r)
            oc[1].add(c)
            oc[2].add(r+c)
            oc[3].add(r-c)            
            for nc in range(n):
                nr = r+1
                if nr not in oc[0] and nc not in oc[1] and (nr+nc) not in oc[2] and (nr-nc) not in oc[3]:
                    DFS(nr, nc, [set(oc[0]),set(oc[1]),set(oc[2]),set(oc[3])], path[:])        
        for c in range(n): DFS(0, c, [set() for _ in range(4)], [])
        return ans 