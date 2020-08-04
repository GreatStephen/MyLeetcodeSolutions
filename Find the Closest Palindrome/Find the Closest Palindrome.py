class Solution:
    def nearestPalindromic(self, S: str) -> str:
        # 把所有可能结果选出来
        # 4个特殊情况，长度为n的 999/10001，长度为(n+1)的 9999/100001
        # 还有前半部分 +1/+0/-1再回文的三种结果。最终结果肯定在其中
        
        K = len(S)
        # special cases
        candidates = [str(10**k + d) for k in (K-1, K) for d in (-1, 1)]
                
        prefix = S[:(K+1)//2]
        for num in (int(prefix)-1, int(prefix), int(prefix)+1):
            suffix = str(num)[::-1]
            if len(S)&1: suffix = suffix[1:]
            candidates.append(str(num)+suffix)
                    
        def difference(a,b):
            return abs(int(a)-int(b))
        
        ans, dif = None, float('inf')
        for c in candidates:
            if c==S: continue
            d = difference(c,S)
            if d<dif:
                ans = c
                dif = d
            elif d==dif and int(c)<int(ans):
                ans = c
                dif = d
        
        
        return ans