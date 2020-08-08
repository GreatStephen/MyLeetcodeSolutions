class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        seen = set()
        if len(s)!=len(t): return False
        
        # def canConvert(s,t,k):
        for i in range(len(s)):
            if s[i]==t[i]: 
                continue
            diff = (ord(t[i])-ord(s[i]))%26
            # print(diff)
            legal = False
            while diff<=k:
                # print(diff)
                if diff in seen:
                    diff += 26
                else:
                    seen.add(diff)
                    legal = True
                    break
            if not legal:
                return False
        
        
        return True
        
            