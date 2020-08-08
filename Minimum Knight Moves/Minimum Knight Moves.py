class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        # BFS超时
        deq = deque()
        deq.append((0,0,0))
        dirs = [[-2,1],[-1,2],[1,2],[2,1],[2,-1],[1,-2],[-1,-2],[-2,-1]]
        
        
        while deq:
            r,c,step = deq.popleft()
            if r==x and c==y:
                return step
            for d in dirs:
                newr, newc = r+d[0], c+d[1]
                deq.append((newr, newc, step+1))
        
        return 0
        