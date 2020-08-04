class Solution:
    def minDifficulty(self, J: List[int], d: int) -> int:
        # DP，以d作为row，以J作为col，把今天的最大max与前一天前面的最小diff相加，往前遍历取最小值
        dp = [[-1]*(len(J)) for i in range(d+1)]
        
        max = 0
        for j in range(len(J)):
            if J[j]>max: max = J[j]
            dp[1][j] = max

        for i in range(2, d+1):
            for j in range(i-1, len(J)):
                max = J[j]
                ans = 10**6
                for k in range(j-1, i-3, -1):
                    ans = min(ans, max+dp[i-1][k])
                    if J[k]> max: max = J[k]
                dp[i][j] = ans
        
        return dp[-1][-1]
                        