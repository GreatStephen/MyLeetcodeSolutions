class Solution(object):
    def minTotalDistance(self, grid):
        # 暴力解，一个tc超时
        R,C = len(grid), len(grid[0])
        homes = []
        for i in range(R):
            for j in range(C):
                if grid[i][j]==1:
                    homes.append([i,j])
        
        def ManDis(i,j):
            ans = 0
            for h in homes:
                ans += abs(h[0]-i)+abs(h[1]-j)
            return ans
        
        
        ans = float('inf')
        for i in range(R):
            for j in range(C):
                ans = min(ans, ManDis(i,j))
        
        
        return ans