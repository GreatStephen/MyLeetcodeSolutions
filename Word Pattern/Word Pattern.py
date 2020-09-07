class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        ss = str.split(' ')
        l_s, s_l = {}, {}
        if len(pattern)!=len(ss):
            return False
        for letter, s in zip(pattern, ss):
            if letter in l_s and s in s_l:
                if l_s[letter]!=s or s_l[s]!=letter: 
                    return False
            elif letter not in l_s and s not in s_l:
                l_s[letter] = s
                s_l[s] = letter
            else:
                return False
        return True