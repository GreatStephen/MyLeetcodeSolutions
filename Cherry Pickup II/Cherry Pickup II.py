class Solution(object):
    def cherryPickup(self, grid):
        # 三维DP，当前row行数，robot1的纵坐标，robot2的纵坐标，把这三个信息组成的最优解放入DP
        # 从当前r1和r2的位置开始，遍历下一行可能的3*3种情况，然后取最大值，加上此行的数值即可

        R,C = len(grid), len(grid[0])
        
        d = [[[-1]*C for i in xrange(C)] for j in xrange(R)]
        def DP(row, r1, r2):
            if d[row][r1][r2]!=-1:
                return d[row][r1][r2]
            if row==R-1:
                d[row][r1][r2] = grid[row][r1]+grid[row][r2] if r1!=r2 else grid[row][r1]
                return d[row][r1][r2]
            ans = 0
            for newr1 in (r1-1, r1, r1+1):
                for newr2 in (r2-1, r2, r2+1):
                    if not (0<=newr1<C and 0<=newr2<C):
                        continue
                    if newr1>newr2:
                        ans = max(ans, DP(row+1, newr2, newr1))
                    else:
                        ans = max(ans, DP(row+1, newr1, newr2))
            ans += grid[row][r1]+grid[row][r2] if r1!=r2 else grid[row][r1]
            d[row][r1][r2] = ans
            return ans
        
        return DP(0, 0, C-1)