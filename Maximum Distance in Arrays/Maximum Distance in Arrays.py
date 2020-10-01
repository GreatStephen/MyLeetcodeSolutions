class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        # 这个方法很巧妙，边更新边查，解决了min和max处于同一个array的问题
        # 每次比较的时候，min和max都是之前的结果，所以不存在共存问题。比完之后把min和max更新，下一次比较仍然不存在共存问题。
        minval, maxval = arrays[0][0], arrays[0][-1]
        ans = 0
        for i in range(1, len(arrays)):
            ans = max(ans, abs(arrays[i][0]-maxval))
            ans = max(ans, abs(arrays[i][-1]-minval))
            minval = min(minval, arrays[i][0])
            maxval = max(maxval, arrays[i][-1])
        return ans