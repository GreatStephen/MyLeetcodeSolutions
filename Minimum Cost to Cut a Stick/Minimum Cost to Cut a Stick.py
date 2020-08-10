class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:     
        
        @lru_cache(None)
        def helper(i, j, l, r):
            if r<l: return 0
            if r==l: return j-i
            cost = j-i
            ans = float('inf')
            for k in range(l, r+1):
                ans = min(ans, helper(i,cuts[k],l,k-1)+helper(cuts[k],j,k+1,r))
            return cost+ans
        
        
        cuts.sort()
        return helper(0, n, 0, len(cuts)-1)
