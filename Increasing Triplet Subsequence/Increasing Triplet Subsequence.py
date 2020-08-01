class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        c1, c2 = 1e100, 1e100
        for n in nums:
            if n<=c1: c1 = n
            elif n<=c2: c2 = n
            else: return True
        return False