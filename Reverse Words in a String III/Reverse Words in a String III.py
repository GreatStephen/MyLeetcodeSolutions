class Solution:
    def reverseWords(self, s: str) -> str:
        ss = s.split(' ')
        ans = ''
        
        for i,v in enumerate(ss):
            ans += v[::-1]
            if i!=len(ss)-1:
                ans += ' '
        
        return ans