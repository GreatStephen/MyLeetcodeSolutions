class Solution:
    def minimumDeletions(self, s: str) -> int:
        a, b = [0]*len(s), [0]*len(s)
        
        num = 0
        for i,c in enumerate(s):
            a[i] = max(num, 0)
            if c=='b': num += 1
        num = 0
        ans = float('inf')
        for i in range(len(s)-1, -1, -1):
            c = s[i]
            b[i] = max(num, 0)
            if c=='a': num += 1
            ans = min(ans, a[i]+b[i])
        
        return ans