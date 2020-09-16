class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lastword = ''
        lastidx = len(s)-1
        while lastidx>=0 and s[lastidx]==' ':
            lastidx -= 1
        for i in range(lastidx, -1, -1):
            if s[i]==' ': break
            lastword = s[i]+lastword
        return len(lastword)