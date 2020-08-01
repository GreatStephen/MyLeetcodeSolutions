class Solution:
    def addDigits(self, num: int) -> int:
        ans = 0
        while num>0:
            ans += num%10
            num //= 10
        if ans//10==0: return ans
        else: return self.addDigits(ans)