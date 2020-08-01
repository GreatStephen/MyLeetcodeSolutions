class Solution:
    def minMoves(self, nums: List[int]) -> int:
        min, sum, ans = 10**10, 0, 0
        for i,v in enumerate(nums):
            if v<min: min = v
            sum += v
            ans = sum-(i+1)*min
        return ans

        # or 1 line but slower
        # return sum(nums)-len(nums)*min(nums)