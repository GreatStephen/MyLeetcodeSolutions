class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        # r维护当前的最大值，如果r==i+1，说明前面所有的灯都凉了，符合条件
        r, ans = 0, 0
        for i,v in enumerate(light):
            r = max(r, v)
            if r==i+1: ans+=1
        return ans