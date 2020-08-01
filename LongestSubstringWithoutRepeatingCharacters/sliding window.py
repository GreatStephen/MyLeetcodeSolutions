class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l, r = 0, 0
        ans = 0
        while r<len(s):
            if s[r] not in seen:
                seen.add(s[r])
                r+=1
                ans = max(ans, r-l)
                continue
            # duplicated element exists
            while s[l]!=s[r]: 
                seen.remove(s[l])
                l+=1
            l+=1 
            r+=1
            ans = max(ans, r-l)
        return ans