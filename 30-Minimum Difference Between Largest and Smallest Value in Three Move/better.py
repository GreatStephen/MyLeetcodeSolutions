class Solution:
    def minDifference(self, nums: List[int]) -> int:
        # 左0右3，左1右2，左2右1，左3右0，只有这四种情况
        if len(nums)<=4: return 0
        nums.sort()
        return min([a-b for a, b in zip(nums[-4:], nums[:4])])