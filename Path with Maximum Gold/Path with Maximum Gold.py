class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        # 普通的DFS
        R,C = len(grid), len(grid[0])
        dirs = [[-1,0],[0,1],[1,0],[0,-1]]
        self.ans = 0
        
        def legal(r,c,g):
            if 0<=r<R and 0<=c<C and g[r][c]!=0:
                return True
            return False
        
        def DFS(r,c,g,res):
            res += g[r][c]
            val = g[r][c]
            self.ans = max(self.ans, res)
            g[r][c] = 0
            for d in dirs:
                newr, newc = r+d[0], c+d[1]
                if legal(newr, newc, g):
                    DFS(newr, newc, g, res)
            g[r][c] = val
        
        
        for i in range(R):
            for j in range(C):
                if grid[i][j]==0: continue
                g = []
                for row in grid:
                    g.append(row[:])
                DFS(i,j,g,0)
        
        return self.ans