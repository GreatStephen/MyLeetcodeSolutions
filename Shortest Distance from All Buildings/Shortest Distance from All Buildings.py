class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        # 每栋房子都做一个BFS，把距离存在matrix里
        # 如果matrix的某一个位置能到所有房子，再算距离是不是最短的
        R, C = len(grid), len(grid[0])
        matrix = [[None]*C for i in range(R)]
        dirs = [(0,-1),(-1,0),(0,1),(1,0)]
        seen = None
        
        def legal(i,j):
            if 0<=i<R and 0<=j<C and grid[i][j]==0 and (i,j) not in seen: 
                return True
            return False
        
        numbuild = 0
        for i in range(R):
            for j in range(C):
                if grid[i][j]==1:
                    numbuild += 1
                    q = deque()
                    q.append((i,j,0))
                    seen = set()
                    while q:
                        r,c,dis = q.popleft()
                        if (r,c) in seen: continue
                        seen.add((r,c))
                        if grid[r][c]==0:
                            if not matrix[r][c]:
                                matrix[r][c] = []
                            matrix[r][c].append(dis)
                        for d in dirs:
                            newr,newc = r+d[0], c+d[1]
                            if legal(newr, newc):
                                q.append((newr,newc,dis+1))
        
        # print(matrix)
        
        ans = 10**9
        for i in range(R):
            for j in range(C):
                if matrix[i][j] and len(matrix[i][j])==numbuild:
                    ans = min(ans, sum(matrix[i][j]))
        
        return ans if ans<10**9 else -1
        