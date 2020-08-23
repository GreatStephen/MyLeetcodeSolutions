class Solution(object):
    def stoneGameV(self, stoneValue):
        
        d = {}
        
        def DP(x,y,score,SUM):
            if x==y:
                return score
            if (x,y) in d:
                return d[(x,y)]
            lsum,rsum = 0, SUM
            ans = 0
            for i in range(x,y):
                lsum += stoneValue[i]
                rsum -= stoneValue[i]
                if lsum>rsum: # throw left
                    ans = max(ans, DP(i+1,y, score+rsum, rsum))
                elif rsum>lsum: # throw right
                    ans = max(ans, DP(x,i, score+lsum, lsum))
                else:
                    ans = max(ans, DP(i+1,y, score+rsum, rsum))
                    ans = max(ans, DP(x,i, score+lsum, lsum))
            d[(x,y)] = ans
            return ans
                    
        
        
        return DP(0,len(stoneValue)-1,0,sum(stoneValue))
[62008,269055,379802,503405,589774]    