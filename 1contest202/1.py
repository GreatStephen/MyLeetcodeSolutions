class Solution(object):
    def threeConsecutiveOdds(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        count = 3
        for a in arr:
            if a&1:
                count -= 1
            else:
                count = 3
            if not count:
                return True
        return False