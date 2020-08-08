class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        N = 1
        idx = 0
        
#         for i,v in enumerate(arr):
#             if v==N: N+=1
#             else:
#                 while v>N:
#                     k-=1
#                     N+=1
#                     if k==0: return N
#                 N+=1
        
#         return N+k
        while k>0:
            if N!=arr[idx]:
                k-=1
            else:
                idx += 1
            N+=1
            if idx==len(arr): break
        return N+k-1