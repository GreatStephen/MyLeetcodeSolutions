class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for i,v in enumerate(nums):
            if v in s:
                return True
            s.add(v)
        return False
        