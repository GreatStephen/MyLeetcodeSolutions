class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        R,C = len(heights), len(heights[0])
        self.ans = float('inf')
        visited = set()
        
        def DFS(r,c,cost):
            if r==R-1 and c==C-1:
                self.ans = min(self.ans, cost)
                return
            for i,j in [[r+1,c], [r-1,c], [r,c+1], [r,c-1]]:
                if 0<=i<R and 0<=j<C and (i, j) not in visited:
                    visited.add((i,j))
                    DFS(i,j,max(0, abs(heights[i][j]-heights[r][c])))
                    visited.remove((i,j))
        
        DFS(0,0,0)
        
        return self.ans