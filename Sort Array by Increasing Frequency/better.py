class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        # 直接按照count的数字排序即可，不需要手动统计
        ct = Counter(nums)
        return sorted(nums, key=lambda x: (ct[x], -x))