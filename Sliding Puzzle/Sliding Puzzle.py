class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        board = (tuple(board[0]), tuple(board[1]))
        visited = {}
        R,C = 2, 3
        pos = {1:[0,0], 2:[0,1], 3:[0,2], 4:[1,0], 5:[1,1], 0:[1,2]}
        end = ((1,2,3),(4,5,0))
        wrong = ((1,2,3),(5,4,0))
        
        def heuristic(board):
            ans = 0
            for i in range(R):
                for j in range(C):
                    if board[i][j]==0:
                        continue
                    ans += abs(pos[board[i][j]][0] - i) + abs(pos[board[i][j]][1] - j)
            return ans
        
        zr, zc = 0,0
        for zr in range(R):
            for zc in range(C):
                if board[zr][zc]==0:
                    break
        
        heap = []
        heapq.heapify(heap)
        visited[board] = 0 + heuristic(board)
        heapq.heappush(heap, (visited[board], 0, board, zr, zc))
        
        while heap:
            cost, depth, b, zr, zc = heapq.heappop(heap)
            if b in visited and visited[b]<cost:
                continue
            if b==end:
                return depth
            elif b==wrong:
                return -1
            for newr,newc in [[zr+1, zc], [zr-1, zc], [zr, zc+1], [zr, zc-1]]:
                if 0<=newr<R and 0<=newc<C:
                    newb = [list(b[0]), list(b[1])]
                    newb[zr][zc], newb[newr][newc] = newb[newr][newc], newb[zr][zc]
                    newb = (tuple(newb[0]), tuple(newb[1]))
                    newcost = depth+1+heuristic(newb)
                    if newb in visited and visited[newb]<=newcost:
                        continue
                    visited[newb] = newcost
                    heapq.heappush(heap, (visited[newb], depth+1, newb, newr, newc))
        
        return -1