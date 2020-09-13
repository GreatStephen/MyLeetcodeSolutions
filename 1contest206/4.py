class Solution:
    def isTransformable(self, s: str, t: str) -> bool:
        # 错误答案
        if not s: return True
        sets, sett = set(), set()
        for i in range(len(s)):
            sets.add(s[i])
            sett.add(t[i])
            if sets==sett:
                if s[:i+1]<t[:i+1]: 
                    return False
                else:
                    return self.isTransformable(s[i+1:], t[i+1:])
        
        return False