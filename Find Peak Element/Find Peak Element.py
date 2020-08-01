class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        lo, hi, neg_inf = 0, len(nums)-1, -1e100
        mid = (lo+hi)//2
        while lo<hi:
            l = nums[mid-1] if mid-1>=0 else neg_inf
            r = nums[mid+1] if mid+1<len(nums) else neg_inf
            m = nums[mid]
            if l<m<r:
                lo = mid+1
                mid = (lo+hi)//2
            elif r<m<l:
                hi = mid-1
                mid = (lo+hi)//2
            elif l>m and r>m:
                lo = mid+1
                mid = (lo+hi)//2
            else:
                # find the peak
                return mid
        return lo
