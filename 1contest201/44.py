class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:     
        
        cuts.sort()
        # ans = 10**9
        
        def helper(n, cuts):
            if not cuts: return 0
            ans = 10**9
            for i,c in enumerate(cuts):
                smaller = cuts[i-1] if i>0 else 0
                bigger = cuts[i+1] if i+1<len(cuts) else n
                ans = min(ans, bigger-smaller+helper(n,cuts[:i]+cuts[i+1:]))
            return ans
        
        
        return helper(n, cuts)

# 36 [13,17,15,18,3,22,27,6,35,7,11,28,26,20,4,5,21,10,8]