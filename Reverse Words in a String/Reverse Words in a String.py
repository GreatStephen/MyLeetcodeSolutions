class Solution:
    def reverseWords(self, s: str) -> str:
        words = [s for s in s.split(' ') if s]
        ans = ''
        for s in reversed(words):
            ans += s + ' '
        return ans[:-1]