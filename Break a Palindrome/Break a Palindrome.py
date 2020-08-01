class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        for i in range(len(palindrome)//2):
            if palindrome[i]!='a':
                palindrome = palindrome[:i]+'a'+palindrome[i+1:]
                return palindrome
        if len(palindrome)==1: return ''
        palindrome = palindrome[:-1]+'b'
        return palindrome