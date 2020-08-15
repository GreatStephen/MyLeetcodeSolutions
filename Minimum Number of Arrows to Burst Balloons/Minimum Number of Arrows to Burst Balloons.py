class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        # greedy. 按end从小到大排序，然后每次打最左侧气球的最右端点
        # 这样可以保证当前箭头可以打到最多的重复气球

        points = sorted(points, key=lambda x:x[1])
        
        ans, idx = 0, 0
        while idx<len(points):
            ans += 1
            pos = points[idx][1]
            idx += 1
            while idx<len(points):
                if points[idx][0]<=pos<=points[idx][1]:
                    idx += 1
                else:
                    break
        
        
        return ans