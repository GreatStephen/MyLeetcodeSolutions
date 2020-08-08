class Solution:
    def longestAwesome(self, s: str) -> int:
        ans = 1
        
        @lru_cache(None)
        def helper(i,j):
            if i==j:
                return {s[i]}
            else:
                lastres = helper(i,j-1)
                if s[j] in lastres:
                    lastres.remove(s[j])
                else:
                    lastres.add(s[j])
            return lastres
        
        
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                res = helper(i,j)
                if len(res)<=1:
                    ans = max(ans, j-i+1)
        
        return ans            
                    