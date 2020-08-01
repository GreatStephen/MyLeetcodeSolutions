class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        MAX = 0x7FFFFFFF
        while b:
            carry = ((a&b)<<1)&mask
            a = (a^b)&mask
            b = carry
        return a if a<MAX else a^(~mask) # 截取前32位