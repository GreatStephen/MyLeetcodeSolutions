class Solution(object):
    def containsCycle(self, grid):
        R,C = len(grid), len(grid[0])
        def DFS(r,c,length,seen):
            char = grid[r][c]
            grid[r][c] = '$'
            for newr,newc in [[r+1,c],[r-1,c],[r,c+1],[r,c-1]]:
                if 0<=newr<R and 0<=newc<C:
                    if (newr,newc) in seen and length-seen[(newr,newc)]+1>=4:
                        # print newr,newc,length,seen
                        return True
                    if grid[newr][newc]==char:
                        seen[(newr,newc)] = length+1
                        if DFS(newr,newc,length+1,seen):
                            return True
            return False
        
        
        
        for i in range(R):
            for j in range(C):
                if grid[i][j] != '$' and DFS(i,j,1,{(i,j):1}):
                    return True
        return False


[["f","a","a","c","b"],["e","a","a","e","c"],["c","f","b","b","b"],["c","e","a","b","e"],["f","e","f","b","f"]]