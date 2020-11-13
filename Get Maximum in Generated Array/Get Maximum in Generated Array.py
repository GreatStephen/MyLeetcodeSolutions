class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n<=1: return n
        nums = [0,1]
        idx = 1
        ans = 0
        
        for i in range(2, n+1):
            if i&1:
                nums.append(nums[idx]+nums[idx+1])
                idx += 1
            else:
                nums.append(nums[idx])
            ans = max(ans, nums[-1])
        return ans