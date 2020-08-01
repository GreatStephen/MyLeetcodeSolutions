class Solution:
    def convertToTitle(self, n: int) -> str:
        # A=1 Z=26 ---> A=0 Z=25，然后变成一个26进制的数字
        ans = ''
        while n!=0:
            ans = chr((n-1)%26 + ord('A')) + ans
            n = (n-1)//26
        return ans