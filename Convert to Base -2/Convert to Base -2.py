class Solution:
    def baseNeg2(self, N: int) -> str:
        # 这题真想不出来，答案也看不懂为什么
        s = []
        while N!=0:
            s.append(N&1)
            N = -(N>>1)
        ans = ''
        while len(s)>0:
            ans+=str(s.pop())
        return ans if len(ans)>0 else '0'