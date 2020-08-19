class Solution(object):
    def hasValidPath(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        # DFS算法，沿着路途走就行了
        # 0:left, 1:right, 2:up, 3:down
        nextmoves = [[1,4,6], [1,3,5], [2,3,4], [2,5,6]]
        nextdirs = [[],[0,1], [2,3], [0,3], [1,3], [0,2], [1,2]]
        dirs = [[0,-1], [0,1], [-1,0], [1,0]]
        
        seen = set([(0,0)])
        R,C = len(grid), len(grid[0])
        
        def DFS(r,c):
            if r==R-1 and c==C-1:
                return True
            for ndir in nextdirs[grid[r][c]]:
                newr, newc = r+dirs[ndir][0], c+dirs[ndir][1]
                if 0<=newr<R and 0<=newc<C and (newr,newc) not in seen and grid[newr][newc] in nextmoves[ndir]:
                    seen.add((newr, newc))
                    if DFS(newr, newc): return True
            return False
        
        
        return DFS(0,0)