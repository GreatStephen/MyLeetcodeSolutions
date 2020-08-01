class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for i in range(32):
            t = n%2
            ans <<= 1
            n >>= 1
            ans += t
        return ans