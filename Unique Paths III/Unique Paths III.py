class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        # 简单的DFS。统计0的数量，只要到达终点时剩余0个0，就说明遍历了所有格子
        # 修改原grid来标记已经走过的点
        R,C = len(grid), len(grid[0])
        start = None
        empty = 0
        for i in range(R):
            for j in range(C):
                if grid[i][j]==1: start = (i,j)
                elif grid[i][j]==0: empty += 1
        
        self.ans = 0
        def DFS(r,c,empty):
            if not (0<=r<R and 0<=c<C and grid[r][c]>=0):
                return
            if grid[r][c]==2:
                if empty==0: self.ans += 1
                return
            
            grid[r][c] = -2
            for newr,newc in [[r+1,c],[r-1,c],[r,c+1],[r,c-1]]:
                DFS(newr, newc, empty-1)
            grid[r][c] = 0
        
        
        
        DFS(start[0], start[1], empty+1)
        return self.ans