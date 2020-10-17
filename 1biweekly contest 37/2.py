class Solution:
    def bestCoordinate(self, towers: List[List[int]], radius: int) -> List[int]:
        
        def dis(x, y):
            return abs(x[0]-y[0])+abs(x[1]-y[1])
        def nq(x, y):
            return math.floor(y[2]/(1+math.sqrt((x[0]-y[0])**2+(x[1]-y[1])**2)))
        def comp(x, y):
            if not x: return y
            if x[0]<y[0]:
                return x
            elif x[0]==y[0]:
                if x[1]<y[1]:
                    return x
                else:
                    return y
            else:
                return y
        
        maxq = 0
        ans = None
        for i in range(len(towers)):
            q = 0
            x = towers[i]
            for j in range(len(towers)):
                y = towers[j]
                if dis(x[:2], y[:2])<=radius:
                    
                    q += nq(x,y)
                    if i==1: print(q)
            # print(q)
            if q>maxq:
                ans = x[:2]
                maxq = q
            elif q==maxq:
                ans = comp(ans, x[:2])
        
        return ans