"aaabbbabbbb"
[3,5,10,7,5,3,5,5,4,8,1]

class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        
        ans = 0
        lastidx = 0
        for i,c in enumerate(s):
            if i==0: continue
            if c==s[i-1]:
                if cost[lastidx]<=cost[i]:
                    ans += cost[lastidx]
                    lastidx = i
                else:
                    ans += cost[i]
            else:
                lastidx = i
        
        return ans