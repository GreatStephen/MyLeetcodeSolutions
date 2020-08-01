class Solution:
    i_offset = [-1, 0, 1, 0]
    j_offset = [0, 1, 0, -1]
    N = 0
    def regionsBySlashes(self, grid: List[str]) -> int:
        self.N = len(grid)
        flag = []
        for i in range(self.N):
            l = []
            for j in range(self.N):
                l.append([0,0,0,0])
            flag.append(l)
        ans = 0
        for i in range(self.N):
            for j in range(self.N):
                for x in range(4):
                    if flag[i][j][x]==0:
                        ans += 1
                        self.DFS(grid, flag, i, j, x)        
        return ans
    
    def DFS(self, grid: List[str], flag, r, c, arr_pos):
        ch = grid[r][c]
        flag[r][c][arr_pos]=1
        if ch==' ':
            if flag[r][c][(arr_pos+1)%4]==0:
                self.DFS(grid, flag, r, c, (arr_pos+1)%4)
            if flag[r][c][(arr_pos-1)%4]==0:
                self.DFS(grid, flag, r, c, (arr_pos-1)%4)
        elif ch=='/':
            if arr_pos==0 or arr_pos==2:
                if flag[r][c][(arr_pos-1)%4]==0:
                    self.DFS(grid, flag, r, c, (arr_pos-1)%4)
            else:
                if flag[r][c][(arr_pos+1)%4]==0:
                    self.DFS(grid, flag, r, c, (arr_pos+1)%4)
        elif ch=='\\':
            if arr_pos==0 or arr_pos==2:
                if flag[r][c][(arr_pos+1)%4]==0:
                    self.DFS(grid, flag, r, c, (arr_pos+1)%4)
            else:
                if flag[r][c][(arr_pos-1)%4]==0:
                    self.DFS(grid, flag, r, c, (arr_pos-1)%4)
        new_r, new_c = r+self.i_offset[arr_pos], c+self.j_offset[arr_pos]
        if new_r>=0 and new_r<self.N and new_c>=0 and new_c<self.N:
            if flag[new_r][new_c][(arr_pos+2)%4]==0:
                self.DFS(grid, flag, new_r, new_c, (arr_pos+2)%4)
