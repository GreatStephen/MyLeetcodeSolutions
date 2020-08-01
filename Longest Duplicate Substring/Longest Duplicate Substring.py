class Solution:
    def longestDupSubstring(self, S: str) -> str:
        lo, hi = 1, len(S)        
        ans = ''
        MOD = 2**63-1 # take a mod, to reduce the number
        
        def helper(length):
            MSB = pow(26, length-1, MOD)
            cur = 0
            seen = set()
            for i in range(length):
                cur *= 26
                cur += (ord(S[i])-ord('a'))
                cur %= MOD
            seen.add(cur)   # initial hash value
            for i in range(length, len(S)):
                # update hash value
                cur %= MSB
                cur = cur*26 + (ord(S[i])-ord('a'))
                cur %= MOD
                if cur not in seen:
                    seen.add(cur)
                else:
                    return (i-length+1, i)
            return None
        
        while lo<=hi:
            mid = (lo+hi+1)//2
            pos = helper(mid)
            if pos:
                ans = S[pos[0]:pos[1]+1]
                lo = mid+1
            else:
                hi = mid-1
        return ans

#"ababababababababab"