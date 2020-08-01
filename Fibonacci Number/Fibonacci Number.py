class Solution:
    def fib(self, N: int) -> int:
        if N==0: return 0
        if N==1: return 1
        ans = [0,1]
        for i in range(2, N+1):
            ans.append(ans[-1]+ans[-2])
        return ans[-1]