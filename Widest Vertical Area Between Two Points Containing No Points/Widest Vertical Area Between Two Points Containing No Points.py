class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        a = sorted(points, key=lambda x: (x[0], x[1]))
        
        ans = 0
        for i in range(len(a)-2):
            ans = max(ans, a[i+1][0]-a[i][0])
        return ans