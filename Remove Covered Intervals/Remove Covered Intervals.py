class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        # 拉不拉东算法，好用。
        # 按start升序，end降序排列。以此来找到[i-1]是否cover [i]。
        # 因为前一个的start必然<=后一个的start。end又降序排列，所以只需检查后一个的end是否<=前一个的end。
        intervals = sorted(intervals, key=lambda x: (x[0], -x[1]))
        
        prev = intervals[0]
        ans = 1
        for i in range(1, len(intervals)):
            cur = intervals[i]
            if prev[0]<=cur[0] and prev[1]>=cur[1]:
                # covered
                continue
            else:
                # not covered
                ans += 1
                prev = cur
        
        return ans