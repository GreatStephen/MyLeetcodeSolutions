class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle)==0: return 0
        def check(check_str, needle):
            if len(check_str)<len(needle): return False
            if check_str[:len(needle)] == needle: return True
            else: return False
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i]==needle[0]:
                if check(haystack[i:], needle): return i
        return -1