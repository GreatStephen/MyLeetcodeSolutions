class Solution:
    def modifyString(self, s: str) -> str:
        cur = 97
        ans = ''
        for i,c in enumerate(s):
            if c=='?':
                left, right = s[i-1] if i>0 else None, s[i+1] if i+1<len(s) else None
                while chr(cur)==left or chr(cur)==right:
                    cur += 1
                    if cur>122: cur = 97
                ans += chr(cur)
                cur += 1
                if cur>122: cur = 97
            else:
                ans += c
        return ans