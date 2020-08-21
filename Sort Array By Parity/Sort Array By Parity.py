class Solution(object):
    def sortArrayByParity(self, A):
        # 两个指针同时向中间移动，l指向第一个奇数，r指向第一个偶数，然后交换l和r
        # 类似quicksort里面的partition
        l,r = 0, len(A)-1
        
        while l<=r:
            while l<=r and not A[l]&1:
                l += 1
            while l<=r and A[r]&1:
                r -= 1
            if not l<=r: break
            A[l], A[r] = A[r], A[l]
            l += 1
            r -= 1
        return A