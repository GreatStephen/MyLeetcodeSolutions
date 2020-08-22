class Solution(object):
    # 这道题把所有的面积（包括左右两个端点）连接起来，作为一个递增数组
    # 在面积总和的范围内产生一个随机数，然后看这个随机数在哪个面积的矩形里
    # 再把这个随机数，用它对应的矩形，产生出两个坐标
    def __init__(self, rects):
        self.l = []
        self.rects = rects
        self.area = 0
        for r in rects:
            self.area += (r[2]-r[0]+1)*(r[3]-r[1]+1) # 面积的累计和
            self.l.append(self.area)
        

    def pick(self):
        randint = random.randint(1, self.area)
        pos = bisect.bisect_left(self.l, randint)
        r = self.rects[pos]
        area = self.l[pos]
        x = r[0] + (area-randint)%(r[2]-r[0]+1)
        y = r[1] + (area-randint)/(r[2]-r[0]+1)
        return [x,y]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()