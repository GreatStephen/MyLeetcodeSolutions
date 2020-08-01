class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if len(nums)==0: return 0
        l, r, sum, ans = 0, -1, 0, 1e100
        while r<len(nums):
            if sum < s:
                r+=1
                if r>=len(nums): break
                sum += nums[r]                
            else:
                ans = min(ans, r-l+1)
                sum -= nums[l]
                l+=1
        if ans==1e100: return 0
        return ans