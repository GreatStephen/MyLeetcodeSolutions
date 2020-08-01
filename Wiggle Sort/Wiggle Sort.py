class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 直接检查奇数位置i是否大于等于i-1，偶数位置i是否小于等于i-1
        # 如果哪个地方错了，直接交换i和i-1
        def swap(nums, i, j):
            t = nums[i]
            nums[i] = nums[i-1]
            nums[i-1] = t
        for i in range(len(nums)):
            if i==0: continue
            if i&1 and nums[i]<nums[i-1]:
                swap(nums, i, i-1)
            elif not i&1 and nums[i]>nums[i-1]:
                swap(nums, i, i-1)