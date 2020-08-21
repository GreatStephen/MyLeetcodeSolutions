class Solution(object):
    def hitBricks(self, grid, hits):
        # 倒序加DFS。先把所有hits都减1，然后从第一行的元素检查有多少个non-dropping孤岛
        # 然后倒序添加hits，每添加一个，检查它自己是否变成non-dropping，如果是的话，从它开始DFS，
        # 把所有和它接触的孤岛全部变成non-dropping。记录这个岛的size。
        # key：检查倒序添加时，每次添加会增加多少个non-dropping元素
        def DFS(r,c):
            if grid[r][c]!=1:
                return 0
            ans = 1
            grid[r][c] = 2
            for newr, newc in [[r+1,c], [r-1,c], [r,c+1], [r,c-1]]:
                if 0<=newr<R and 0<=newc<C:
                    ans += DFS(newr, newc)
            return ans
        
        R,C = len(grid), len(grid[0])
        for r,c in hits:
            grid[r][c] -= 1
        for c in xrange(C):
            DFS(0, c)
        
        
        ans = []
        for r,c in hits[::-1]:
            if grid[r][c]<0:
                grid[r][c] = 0
                ans.insert(0,0)
                continue
            grid[r][c] = 1
            res = 0
            for newr,newc in [[r+1,c], [r-1,c], [r,c+1], [r,c-1]]:
                if 0<=newr<R and 0<=newc<C and grid[newr][newc]==2 or r==0:
                    res = DFS(r,c)-1
                    break
            ans.insert(0,res)
        
        return ans