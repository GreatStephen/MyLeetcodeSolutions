class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        # BFS，这题原理其实也很简单，BFS的层数等于修改的次数
        # 当不用修改时，顺着(0,0)的方向一直找下去，这些点都是修改0次能到达的点
        # 遍历deque，把里面每个点的另外三个方向放进deq，修改次数也加一。重复直到到达终点。
        # 需要注意的是，修改次数加一时，也要顺着新点走完所有路径，路径上的点都是当前修改次数的点。不能只加一个进去，顺着路径走是不增加cost的。
        R,C = len(grid), len(grid[0])
        dirs = [[],[0,1],[0,-1],[1,0],[-1,0]]
        deq = deque()
        def legal(r,c):
            if 0<=r<R and 0<=c<C and grid[r][c]>0:
                return True
            return False
        
        r = c = 0
        while legal(r, c):            
            deq.append((r,c,0))
            newdir = grid[r][c]
            grid[r][c] = -1
            r += dirs[newdir][0]
            c += dirs[newdir][1]
            
        # print(deq)
        while deq:
            r,c,dis = deq.popleft()
            if r==R-1 and c==C-1: return dis
            for i in range(1,5):
                newr,newc = r+dirs[i][0], c+dirs[i][1]
                while legal(newr, newc): # 一定要顺着新点走完一遍，新路径上的点都是dis+1的点，全部放进deq
                    deq.append((newr,newc,dis+1))
                    newdir = grid[newr][newc]                    
                    grid[newr][newc] = -1
                    newr += dirs[newdir][0]
                    newc += dirs[newdir][1]
        
        return 0