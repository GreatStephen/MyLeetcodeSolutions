class Solution:
    def titleToNumber(self, s: str) -> int:
        count = 0
        ans = 0
        while s:
            ans += (ord(s[-1])-64) * (26**count)
            count += 1
            s = s[:-1]
        return ans