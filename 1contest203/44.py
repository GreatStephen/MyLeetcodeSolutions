class Solution(object):
    def stoneGameV(self, stoneValue):
        
        d = {}
        
        def DP(x,y,SUM):
            if x==y:
                return 0
            if (x,y) in d:
                return d[(x,y)]
            lsum,rsum = 0, SUM
            ans = 0
            for i in range(x,y):
                lsum += stoneValue[i]
                rsum -= stoneValue[i]
                if lsum>rsum: # throw left
                    ans = max(ans, rsum+DP(i+1,y, rsum))
                elif rsum>lsum: # throw right
                    ans = max(ans, lsum+DP(x,i, lsum))
                else:
                    ans = max(ans, rsum+DP(i+1,y, rsum))
                    ans = max(ans, lsum+DP(x,i, lsum))
            d[(x,y)] = ans
            return ans
                    
        
        
        return DP(0,len(stoneValue)-1,sum(stoneValue))
        