class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l, r = 0, 0
        ans = 0
        cur = 1
        while r<len(nums):
            # 滑动窗口，对每一个r，找到最靠左的l，使其满足条件，然后r-l即为当前长度
            cur *= nums[r]
            r += 1
            while cur>=k and l<r:
                cur /= nums[l]
                l += 1
            ans += r-l
        return ans