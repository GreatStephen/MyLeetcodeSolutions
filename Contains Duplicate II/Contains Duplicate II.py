class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        s = set()
        for i,v in enumerate(nums):
            if i>k:
                s.remove(nums[i-k-1])
            if v in s:
                return True
            s.add(v)
        return False
        