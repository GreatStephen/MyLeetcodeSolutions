class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        while num>0:
            if num==1: return True
            if num&3: return False
            num >>= 2
        return False