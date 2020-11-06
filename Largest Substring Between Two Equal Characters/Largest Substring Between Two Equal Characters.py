class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        idx = [None]*26
        base = ord('a')
        ans = -1
        for i,c in enumerate(s):
            if idx[ord(c)-base]!=None:
                ans = max(ans, i-idx[ord(c)-base]-1)
            else:
                idx[ord(c)-base] = i
        return ans