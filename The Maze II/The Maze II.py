class Solution:          
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        # Dijkstra Algorithm
        class Item():
            def __init__(self, r, c, dis):
                self.r = r
                self.c = c
                self.dis = dis
            def __lt__(self, other):
                if self.dis<other.dis: return True
                else: return False
            def __str__(self):
                return str((self.r,self.c,self.dis))
            def __repr__(self):
                return str((self.r,self.c,self.dis))
        
        h, seen, o = [], set(tuple(start)), ((-1,0),(0,1),(1,0),(0,-1))
        R, C = len(maze), len(maze[0])
        heapq.heapify(h)
        heapq.heappush(h, Item(start[0], start[1], 0))
        while len(h)>0:
            item = heapq.heappop(h)
            seen.add((item.r, item.c))
            for i in range(4):
                steps = 0
                new_cur, t = None, (item.r+o[i][0], item.c+o[i][1])
                while 0<=t[0]<R and 0<=t[1]<C and maze[t[0]][t[1]]==0:
                    new_cur = t
                    steps += 1
                    t = (t[0]+o[i][0], t[1]+o[i][1])
                if new_cur and new_cur not in seen:
                    if new_cur==tuple(destination): return item.dis+steps
                    new_item = Item(new_cur[0], new_cur[1], item.dis+steps)
                    heapq.heappush(h, new_item)
        return -1