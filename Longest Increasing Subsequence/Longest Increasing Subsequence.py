class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # 经典DP问题。dp[i]=长度为i的递增子串的最大的那个数，这个数保持更新为已遍历过的数字里面的最小的。
        dp = []
        for n in nums:
            pos = bisect.bisect_left(dp, n)
            if pos==len(dp): dp.append(n)
            else: dp[pos] = n
        return len(dp)