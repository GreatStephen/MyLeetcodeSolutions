class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        cum = []
        for i in range(len(nums)):
            if i==0:
                cum.append(nums[i])
            else:
                cum.append(nums[i]+cum[-1])
        
        ans = 0
        for i in range(len(nums)-2):
            left = cum[i]
            mid_left = bisect.bisect_left(cum, left*2)
            mid_left = max(i+1, mid_left)
            mid_right = bisect.bisect_right(cum, left+(cum[-1]-left)/2)
            mid_right = min(len(nums)-1, mid_right)
            # print(mid_left, mid_right)
            ans += max(mid_right-mid_left, 0)
        
        return ans%(10**9+7)
                