class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        if k<=0: k=1
        diff, diff_sum = [0], [0]
        for i in range(len(nums)-1):
            diff.append(nums[i+1]-nums[i]-1)
            diff_sum.append(diff[-1]+diff_sum[-1])
        # print(diff, diff_sum)
        
        idx = bisect.bisect_left(diff_sum, k)
        ans = nums[idx-1] + k - diff_sum[idx-1]


        return ans