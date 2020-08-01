class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        lo, hi = matrix[0][0], matrix[-1][-1]
        mid = (lo+hi)//2

        # find how many numbers are less than or equal to mid
        def findLessOrEqual(mid):
            ans = 0
            for i in range(len(matrix)):
                count = bisect.bisect(matrix[i], mid)
                ans += count
            return ans
            
        while lo<hi:
            mid = (lo+hi)//2
            ct = findLessOrEqual(mid)
            if ct>=k: hi = mid
            else: lo = mid+1
        return lo