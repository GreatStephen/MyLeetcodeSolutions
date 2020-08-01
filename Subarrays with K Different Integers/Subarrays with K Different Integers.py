class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        # Lee的atMost函数
        def atMost(A, K):
            l = r = ans = 0
            seen = collections.defaultdict(int)
            for r in range(len(A)):
                seen[A[r]] += 1
                while len(seen)>K:
                    seen[A[l]] -= 1
                    if seen[A[l]]==0: del seen[A[l]]
                    l+=1
                ans += r-l+1
            return ans
        return atMost(A,K)-atMost(A,K-1)
                    
                