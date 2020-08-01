class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        deq = collections.deque()
        deq.append(tuple(start))
        offset = ((-1,0),(0,1),(1,0),(0,-1))
        R,C = len(maze), len(maze[0])
        
        while len(deq)>0:
            N = len(deq)
            for _ in range(N):
                cur = deq.popleft()
                if cur==tuple(destination): return True
                maze[cur[0]][cur[1]] = 2
                for i in range(4):
                    new_cur = None
                    cur_temp = (cur[0]+offset[i][0], cur[1]+offset[i][1])
                    while 0<=cur_temp[0]<R and 0<=cur_temp[1]<C and maze[cur_temp[0]][cur_temp[1]]!=1:
                        new_cur = cur_temp
                        cur_temp = (cur_temp[0]+offset[i][0], cur_temp[1]+offset[i][1])
                    if new_cur and maze[new_cur[0]][new_cur[1]]!=2: deq.append(new_cur)
        
        
        return False