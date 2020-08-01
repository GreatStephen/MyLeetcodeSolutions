class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans, self.g = 0, grid
        self.R, self.C, self.r_off, self.c_off = len(grid), len(grid[0]), [-1,0,1,0], [0,1,0,-1]
        
        def DFS(r, c, temp_res):
            self.g[r][c] = 0
            temp_res += 1
            for i in range(4):
                new_r, new_c = r+self.r_off[i], c+self.c_off[i]
                if 0<=new_r<self.R and 0<=new_c<self.C and self.g[new_r][new_c]==1:
                    temp_res = DFS(new_r, new_c, temp_res)
            return temp_res
        
        for i in range(self.R):
            for j in range(self.C):
                if(grid[i][j]==1):
                    ans = max(ans, DFS(i, j, 0))
        return ans            
        