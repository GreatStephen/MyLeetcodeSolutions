class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word)==1: return True
        def helper(word, cap):
            if not word: return True
            lo, hi = 65 if cap else 97, 90 if cap else 122
            for w in word:
                if ord(w)<lo or ord(w)>hi: return False
            return True
        
        if 65<=ord(word[0])<=90:
            if 65<=ord(word[1])<=90: return helper(word[2:], True)
            elif 97<=ord(word[1])<=122: return helper(word[2:], False)
        else:
            return helper(word[1:], False)