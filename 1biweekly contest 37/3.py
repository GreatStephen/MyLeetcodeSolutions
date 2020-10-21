from scipy.special import comb, perm

class Solution:
    def numberOfSets(self, num: int, kk: int) -> int:
        MOD = 10**9+7
        
        d = {}
        def dp(n, k):
            if n==k:
                return 1
            if (n,k) in d:
                return d[(n,k)]
            ans = comb(n,k) + (n-1)*dp(n-1, k)
            d[(n,k)] = int(ans)
            return d[(n,k)]
        
        
        
        return dp(num-1, kk)