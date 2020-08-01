class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # DP, dp[i]代表s[0:i]是否合格。对每一位长度的s，检查是否能分成dp[j] and [j:i]在字典中即可
        dp = [True]
        for i in range(len(s)):
            dp.append(False)
            for j in range(i+1):
                val = dp[j] and s[j:i+1] in wordDict
                if val:
                    dp[-1]=True
                    break
        return dp[-1]