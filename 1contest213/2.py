class Solution:
    def countVowelStrings(self, n: int) -> int:
        e = ['a','e','i','o','u']
        
        @lru_cache(None)
        def helper(start, length):
            if length==0:
                return 1
            if start=='u':
                return 1
            ans = 0
            for i in range(e.index(start), 5):
                # print(i)
                ans += helper(e[i], length-1)
            return ans
        
        return helper('a', n)
            