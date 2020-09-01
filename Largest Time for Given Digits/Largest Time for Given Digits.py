class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        # 枚举法。枚举所有的hour和minute，然后取其中的最大值
        self.hour, self.minute = -1, -1
        def helper(x,y,nums):
            hh = [10*nums[x]+nums[y], 10*nums[y]+nums[x]]
            nums.pop(y)
            nums.pop(x)
            mm = [10*nums[0]+nums[1], 10*nums[1]+nums[0]]
            
            for h in hh:
                for m in mm:
                    if h>=24 or m>=60:
                        continue
                    if h>self.hour or h==self.hour and m>self.minute:
                        self.hour, self.minute = h, m
        
        
        for i in range(len(A)-1):
            for j in range(i+1, len(A)):
                helper(i,j, A[:])
        h = str(self.hour) if self.hour>=10 else '0'+str(self.hour)
        m = str(self.minute) if self.minute>=10 else '0'+str(self.minute)
        if self.hour<0:
            return ''
        else:
            return h+':'+m