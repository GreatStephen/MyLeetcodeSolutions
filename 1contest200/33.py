class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        N = len(grid)
        l = []
        for i in range(N):
            count = 0
            row = grid[i]
            for j in range(N-1, -1, -1):
                if row[j]==0: count+=1
                else: 
                    l.append(count)
                    count = -1
                    break
            if count>=0: l.append(count)
        # print(l)
        
        # 如果l[i]不符合这一行要求的0的个数，就往下找到第一个[j]满足要求的，将j和[i:j]之间的全部交换
        # 然后更新l，将[i:j]下沉到j的位置，继续循环
        ans = 0
        for i in range(N):
            target = N-1-i
            if l[i]>=target: continue
            idx = -1
            for j in range(i+1, N):
                if l[j]>=target:
                    ans += j-i
                    idx = j
                    break
            if idx==-1: return -1
            for j in range(idx, i, -1):
                l[j] = l[j-1]
        
        return ans 