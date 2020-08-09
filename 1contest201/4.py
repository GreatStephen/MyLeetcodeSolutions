class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        
        
        def helper(start, n, cuts):
            if not cuts: return 0
            cost = n-start
            ans = 10**9
            for i,c in enumerate(cuts):
                ans = min(ans, cost+helper(start, c, cuts[:i])+helper(c, n, cuts[i+1:]))
            return ans
        
        
        cuts.sort()
        return helper(0, n, cuts)

# 30 [13,25,16,20,26,5,27,8,23,14,6,15,21,24,29,1,19,9,3]