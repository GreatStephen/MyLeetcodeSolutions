class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowel = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        def count(s):
            ans = 0
            for c in s:
                if c in vowel:
                    ans += 1
            return ans
        
        l = len(s)
        return count(s[:l//2])==count(s[l//2:])