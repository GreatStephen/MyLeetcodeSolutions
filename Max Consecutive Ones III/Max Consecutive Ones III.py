class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        l, r, count = 0, 0, K
        ans = 0
        while r<len(A):
            if A[r]==0: count-=1
            if count>=0:
                ans = max(ans, r-l+1)
            else:
                while A[l]==1:
                    l+=1
                l+=1
                count+=1
                ans = max(ans, r-l+1)
            r += 1
        return ans