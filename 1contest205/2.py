class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        sq1, sq2 = list(map(lambda x: x**2, nums1)), list(map(lambda x:x**2, nums2))
        # print(sq1, sq2)
        
        prod1, prod2 = {}, {}
        for k in range(1, len(nums1)):
            for j in range(k):
                n = nums1[j]*nums1[k]
                if n not in prod1:
                    prod1[n] = 0
                prod1[n] += 1
        
        for k in range(1, len(nums2)):
            for j in range(k):
                n = nums2[j]*nums2[k]
                if n not in prod2:
                    prod2[n] = 0
                prod2[n] += 1
        
        # print(prod1, prod2)
        ans = 0
        for sq in sq1:
            if sq in prod2:
                ans += prod2[sq]
        for sq in sq2:
            if sq in prod1:
                ans += prod1[sq]
        return ans