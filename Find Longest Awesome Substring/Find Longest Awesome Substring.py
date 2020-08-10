class Solution:
    def longestAwesome(self, s: str) -> int:
        ans = 0
        
        cur = 0
        seen = [-1]+[len(s)]*1024
        
        for i,c in enumerate(s):
            cur ^= 1<<int(c) # current bitmask
            for bit in range(10): # one bit different is also OK
                ans = max(ans, i-seen[cur^(1<<bit)])
            ans = max(ans, i-seen[cur])
            seen[cur] = min(seen[cur], i)
        
        return ans            
                    