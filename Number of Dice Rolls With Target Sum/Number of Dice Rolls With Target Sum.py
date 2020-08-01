class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        # 正常的二维dp，i是骰子数量，j是有多少种组合的sum=j
        dp = [1]*f+[0]*max(0, target-f)
        # print(dp)
        for i in range(1,d):
            tempdp = [0]*len(dp)
            for j in range(i, len(dp)):
                for k in range(1,f+1):
                    if j-k>=0: tempdp[j]+=dp[j-k]
                    else: break
            dp = tempdp
            # print(dp)
        return dp[target-1]%(10**9+7)