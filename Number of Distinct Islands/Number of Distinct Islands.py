class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        # transform the shape into a str
        # str of directions
        ans = 0
        r_offset = [-1,0,1,0]
        c_offset = [0,1,0,-1]
        s_offset = ['U','R','D','L']
        R = len(grid)
        C = len(grid[0])
        def DFS(grid, r, c, strval):
            grid[r][c] = 0
            for i in range(4):
                new_r = r+r_offset[i]
                new_c = c+c_offset[i]
                if new_r>=0 and new_r<R and new_c>=0 and new_c<C and grid[new_r][new_c]==1:
                    strval += s_offset[i]
                    # print(strval)
                    strval = DFS(grid, new_r, new_c, strval)
            strval += 'B'   # need this BACKTRACKING symbol
            return strval
        
        str_l = []
        for i in range(R):
            for j in range(C):
                if grid[i][j]==1:
                    str_island = DFS(grid, i, j, '')
                    str_l.append(str_island)
        ans = set(str_l)
        return len(ans)