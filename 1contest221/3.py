class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        R,C = len(grid), len(grid[0])
        ans = []
        
        def DFS(r,c):
            if r==R:
                return c
            if grid[r][c]==1:
                if c+1<C and grid[r][c+1]==1:
                    return DFS(r+1, c+1)
            else:
                if c-1>=0 and grid[r][c-1]==-1:
                    return DFS(r+1, c-1)
            return -1
            
            
        
        for c in range(C):
            ans.append(DFS(0,c))
        return ans