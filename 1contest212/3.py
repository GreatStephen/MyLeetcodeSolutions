class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        R,C = len(heights), len(heights[0])
        mem = [[None] * C for i in range(R)]
        visited = set()
        
        def dp(r, c):
            if mem[r][c]!=None:
                return mem[r][c]
            ans = float('inf')
            for newr, newc in [[r+1,c], [r-1,c], [r,c+1], [r,c-1]]:
                if 0<=newr<R and 0<=newc<C and (newr, newc) not in visited:
                    visited.add((newr, newc))
                    ans = min(ans, abs(heights[r][c]-heights[newr][newc])+dp(newr, newc))
                    visited.remove((newr,newc))
            mem[r][c] = ans
            return mem[r][c]
        
        a = dp(0,0)
        return a