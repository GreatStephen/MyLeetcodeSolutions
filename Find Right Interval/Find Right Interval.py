class Solution(object):
    def findRightInterval(self, intervals):
        # 把所有start time和原始下标存起来，再sort
        # 用BS从这里面找当前的end time，如果找到，则取找到的那个下标。没找到就取-1
        
        arr = []
        for i,inter in enumerate(intervals):
            arr.append([inter[0], i])
        arr.sort()
        
        ans = []
        for inter in intervals:
            pos = bisect.bisect_left(arr, [inter[1],0])
            if pos==len(arr):
                ans.append(-1)
            else:
                ans.append(arr[pos][1])
            
        return ans
        