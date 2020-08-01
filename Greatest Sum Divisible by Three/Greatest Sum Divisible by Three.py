class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        # 以余数作为额外信息，构建二维dp
        dp = [0,0,0]
        for n in nums:
            temp = dp[:]
            for r in dp:
                temp[(r+n)%3] = max(temp[(r+n)%3], r+n)
            dp = temp
        return dp[0]