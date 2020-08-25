class Solution(object):
    def canAttendMeetings(self, intervals):
        # 按开始时间排序，然后检查后一个的开始时间是否晚于前一个的结束时间
        intervals.sort()
        for i in range(1, len(intervals)):
            if not intervals[i][0]>=intervals[i-1][1]:
                return False
            
        return True