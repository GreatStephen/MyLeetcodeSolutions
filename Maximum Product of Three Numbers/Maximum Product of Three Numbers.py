class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        # 数学方法，最大三个数相乘，最小两个数乘最大数，取二者最大值
        nums.sort()
        return max(nums[-1]*nums[-2]*nums[-3], nums[0]*nums[1]*nums[-1])