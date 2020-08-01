class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        left, right = [], []
        deq = collections.deque()
        deq.append((0,0))
        for i,n in enumerate(A):
            while deq[-1][0]>n:     # strictly bigger
                deq.pop()
            left.append((i+1)-deq[-1][1])
            deq.append((n, i+1))
        # print(left)
        
        deq.clear()
        deq.append((0,0))
        for i,n in enumerate(reversed(A)):
            while deq[-1][0]>=n:    # bigger than or equal to
                deq.pop()
            right.insert(0, (i+1)-deq[-1][1])
            deq.append((n, i+1))
        # print(right)
        
        ans, MOD = 0, 10**9+7
        for i in range(len(A)):
            ans+= A[i]*left[i]*right[i]
        return ans%MOD