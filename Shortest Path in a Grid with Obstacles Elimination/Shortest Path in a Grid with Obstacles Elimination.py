class Solution(object):
    def shortestPath(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        # 将剩余的k也作为seen的一个元素。
        # 有一个重要的剪纸方法，当剩余k>=((R-1-i)+(C-1-j))时，一定能走通，因为剩余的k很大，保证无论遇到多少个1都能化解
        R,C = len(grid), len(grid[0])
        deq = deque()
        seen = set((0,0,k))
        deq.append((0,0,0,k))
        
        while deq:
            r,c,steps,k = deq.popleft()
            if r==R-1 and c==C-1:
                return steps
            for newr, newc in [[r-1,c],[r+1,c],[r,c-1],[r,c+1]]:
                if 0<=newr<R and 0<=newc<C:
                    newk = k-grid[newr][newc]
                    if (newr, newc, newk) not in seen and newk>=0:
                        deq.append((newr, newc, steps+1, newk))
                        seen.add((newr, newc, newk))
        
        return -1