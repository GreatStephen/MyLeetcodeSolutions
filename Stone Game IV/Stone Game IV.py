class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        lib = [i*i for i in range(1, int(math.sqrt(n))+1)]
        # print(int(math.sqrt(n)))

        dp = [False]
        for i in range(1, n+1):
            dp.append(False)
            for j in range(int(math.sqrt(i))):
                if lib[j]>i: break
                if not dp[i-lib[j]]:
                    dp[-1] = True
                    break
        return dp[-1]