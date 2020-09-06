"bbbaaa"
[4,9,3,8,8,9]

class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        minimum = 0
        cur = '*'
        l, r = 0, 0
        
        ans = 0
        for i,c in enumerate(s):
            if c!=cur:
                if r!=l:
                    ans += minimum
                l = r = i
                minimum = cost[i]
                cur = c
            else:
                r += 1
                minimum = min(minimum, cost[i])
        
        if r!=l:
            ans += minimum
        
        
        return ans