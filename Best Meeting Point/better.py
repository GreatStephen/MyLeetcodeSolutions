class Solution(object):
    def minTotalDistance(self, grid):
        # 这道题很巧妙，把所有横坐标放进一个list，纵坐标放进一个list，然后保证这两个list是sorted
        # 然后，只有point位于这个list中间的位置，才能达到最小。利用这个性质，分别从两个list的中部向外扩展
        # 计算每一对元素之间的差，求和。两个list分别求和，再相加，即为最小值
        R,C = len(grid), len(grid[0])
        vert, hori = [], []
        
        for i in range(R):
            for j in range(C):
                if grid[i][j]==1:
                    vert.append(i)
                    hori.append(j)
        
        # vert默认已经是sorted的了
        hori.sort()
        def find_length(mid, arr):
            ans, r = 0, 0 # mid和r分别从中部向左和向右扩展
            if len(arr)&1:
                r = mid
            else:
                r = mid+1
            while mid>=0:
                ans += arr[r]-arr[mid]
                mid-=1
                r += 1
            return ans
            
        ans, mid = 0, (len(vert)-1)/2
        ans += find_length(mid, vert) # 求vert的最小差值
        mid = (len(hori)-1)/2
        ans += find_length(mid, hori) # 求hori的最小差值
        
        
        return ans