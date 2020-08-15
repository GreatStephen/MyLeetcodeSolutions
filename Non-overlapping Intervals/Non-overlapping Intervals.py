class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        # 经典greedy题，interval scheduler，
        # 按end从小到大排序，每次都选合格的end最小的。最后结果即为可以留下的最大数字
        
        inter = sorted(intervals, key=lambda x:x[1])
        
        count, end = 0, float('-inf')
        for i in inter:
            if i[0]>=end:
                count += 1
                end = i[1]
        
        return len(inter)-count