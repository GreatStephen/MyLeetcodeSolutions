class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        a = x^y
        ans = 0
        while a:
            a &= (a-1)
            ans += 1
        return ans