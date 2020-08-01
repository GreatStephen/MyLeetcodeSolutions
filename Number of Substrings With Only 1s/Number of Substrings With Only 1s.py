class Solution:
    def numSub(self, s: str) -> int:
        ans, MOD = 0, 10**9+7
        ss = s.split('0')
        ss = [sss for sss in ss if len(sss)>0]
        for sss in ss:
            ans += (len(sss)*(len(sss)+1)//2)
            ans %= MOD
        return ans