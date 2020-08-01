class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        nums = [1]+nums+[1]
        dp = [[0]*(len(nums)) for i in range(len(nums))]
        for k in range(2, len(nums)):
            for l in range(len(nums)-k):
                r = l + k
                for i in range(l+1, r):
                    dp[l][r] = max(dp[l][r], nums[l]*nums[i]*nums[r]+dp[l][i]+dp[i][r])
        
        return dp[0][len(nums)-1]
        