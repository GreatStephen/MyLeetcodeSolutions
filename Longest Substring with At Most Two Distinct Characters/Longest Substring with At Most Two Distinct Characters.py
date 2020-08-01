class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        l, r, k = 0, 0, 2
        d = {}
        ans = 0
        while r<len(s):
            if s[r] not in d:
                d[s[r]] = 1
                k -= 1
            else: d[s[r]] += 1
            r += 1
            if k>0: 
                ans = max(ans, r-l)
                continue # find a string with 2 unique chars
            if k<0: # 3 unique chars, move l until only 2 left
                while d[s[l]]>1:
                    d[s[l]] -= 1
                    l += 1
                del d[s[l]]
                l += 1
                k += 1
            if k==0: # exactly 2 unique chars
                ans = max(ans, r-l)
        return ans    