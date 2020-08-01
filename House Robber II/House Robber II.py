class Solution:
    def rob(self, nums: List[int]) -> int:
        # 只有两种情况，0->倒数第二个，1->最后一个，取最大值
        if len(nums)==1: return nums[0]
        def helper(nums: List[int]) -> int:
            p1, p2 = 0, 0
            for n in nums:
                t = p1
                p1 = max(p1, p2+n)
                p2 = t
            return p1        
        return max(helper(nums[:-1]), helper(nums[1:]))