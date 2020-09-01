class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        # 这题他妈无语，最多只需要2次更新，就能孤立出一个岛。
        R,C = len(grid), len(grid[0])
        def helper(grid): # 检查grid有几个岛。
            seen = set()
            ans = 0
            def DFS(r,c):
                for newr, newc in [[r+1,c],[r-1,c],[r,c+1],[r,c-1]]:
                    if 0<=newr<R and 0<=newc<C and (newr,newc) not in seen and grid[newr][newc]==1:
                        seen.add((newr,newc))
                        DFS(newr, newc)
                
            for i in range(R):
                for j in range(C):
                    if grid[i][j]==1 and (i,j) not in seen:
                        seen.add((i,j))
                        DFS(i,j)
                        ans += 1
                        if ans==2: return 2 # 剪枝，如果存在>=2个岛，直接返回2，不需要DFS全部
            return ans
        
        if helper(grid)==2:# 已经存在多个岛，返回0
            return 0
        
        for i in range(R):
            for j in range(C):
                if grid[i][j]==1: # 变一个1为0，然后看看能否孤立一个岛，如果可以就返回1
                    grid[i][j]=0
                    if helper(grid)==2:
                        return 1
                    grid[i][j]=1
        
        return 2 # 前面都不行，那么2绝对可以