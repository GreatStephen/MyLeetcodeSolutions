class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        N = len(A)
        la, lb = [], []
        for i in range(N):
            for j in range(N):
                if A[i][j]:
                    la.append([i,j])
        for i in range(N):
            for j in range(N):
                if B[i][j]:
                    lb.append([i,j])
        
        def dis(a,b):
            return (a[0]-b[0], a[1]-b[1])
        
        # print(la, lb)
        ct = collections.Counter(dis(a,b) for a in la for b in lb)
        # print(ct)
        return max(ct.values() or [0])