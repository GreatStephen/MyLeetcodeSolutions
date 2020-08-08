class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        seen = {}
        if len(s)!=len(t): return False
        
        for i in range(len(s)):
            if s[i]==t[i]: 
                continue
            diff = (ord(t[i])-ord(s[i]))%26
            if diff not in seen:
                if diff <=k: seen[diff] = diff
                else: seen[diff] = k+1
            if seen[diff]<=k:
                seen[diff] += 26
            else: return False
            
            # print(seen)
            
        
        
        return True
        
            