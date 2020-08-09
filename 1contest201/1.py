class Solution:
    def makeGood(self, s: str) -> str:
        notdone = True
        while notdone:
            notdone = False
            i = 0
            while i<len(s)-1:
                if abs(ord(s[i])-ord(s[i+1]))==32:
                    s = s[:i]+s[i+2:]
                    notdone = True
                i += 1
        
        return s
            