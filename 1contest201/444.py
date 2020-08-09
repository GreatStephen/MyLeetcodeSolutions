
class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:     
        
        cuts.sort()
        
        def helper(n, cuts):
            if not cuts: return 0
            idx, smallest =[], 10**9
            for i,c in enumerate(cuts):
                smaller = cuts[i-1] if i>0 else 0
                bigger = cuts[i+1] if i+1<len(cuts) else n
                if bigger-smaller < smallest:
                    idx = [i]
                    smallest = bigger-smaller
                elif bigger-smaller==smallest:                    
                    idx.append(i)
            
            ans = 10**9
            for idxx in idx:
                ans = min(ans, smallest+helper(n, cuts[:idxx]+cuts[idxx+1:]))
            return ans
        
        
        return helper(n, cuts)