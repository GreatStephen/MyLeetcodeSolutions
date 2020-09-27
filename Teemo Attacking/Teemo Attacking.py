class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        idx, last = 0, -1
        ans = 0
        for i,t in enumerate(timeSeries):
            ans += min(duration, (timeSeries[i+1] if i<len(timeSeries)-1 else float('inf'))-timeSeries[i])
        return ans