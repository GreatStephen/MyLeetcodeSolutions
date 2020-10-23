class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 二分查找，将两组数等分成两部分，左边部分的最大值必须小于等于右边部分的最小值
        # 先剔除某个数组为空的情况
        if not nums1: 
            if len(nums2)&1: return nums2[len(nums2)//2]
            else: return (nums2[len(nums2)//2-1] + nums2[len(nums2)//2])/2
        if not nums2: 
            if len(nums1)&1: return nums1[len(nums1)//2]
            else: return (nums1[len(nums1)//2-1] + nums1[len(nums1)//2])/2
        if len(nums1)>len(nums2):
            nums1, nums2 = nums2, nums1
        totallen = len(nums1)+len(nums2)
        
        lo, hi = 0, len(nums1)
        half = (totallen+1)//2
        while lo<=hi:
            mid = (lo+hi)//2
            pos = half-(mid+1)-1
            if mid+1<len(nums1) and nums1[mid+1]<nums2[half-(mid+1)-1]:
                lo = mid+1
            elif nums1[mid]>nums2[pos+1]:
                hi = mid-1
            else:
                lo = mid
                break
        # p1是nums1左半部分的最右端下标。如果p1等于-1说明nums1不贡献值
        p1 = lo if lo<=hi else -1 
        # p2是nums2左半部分的最右端下标。p2+1有可能超出list范围。
        p2 = half-(p1+1)-1
        
        # n1是左半部分的最大值
        n1 = max(nums1[p1] if 0<=p1 else -10**6-1, nums2[p2] if 0<=p2 else -10**6-1)
        # n2是右半部分的最小值
        n2 = min(nums1[p1+1] if p1+1<len(nums1) else 10**6+1, nums2[p2+1] if p2+1<len(nums2) else 10**6+1)
        
        # 通过判断奇数偶数，从n1 n2中取值
        return n1 if totallen&1 else (n1+n2)/2
            
            