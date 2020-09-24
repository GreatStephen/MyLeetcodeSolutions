class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ct = Counter(s)
        for c in t:
            ct[c] -= 1
        for c in ct.keys():
            if ct[c]!=0:
                return c