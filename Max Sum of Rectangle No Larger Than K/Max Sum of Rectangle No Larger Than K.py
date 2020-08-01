class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        R, C = len(matrix), len(matrix[0]) 
        ans = -10**9
        for u in range(R):
            temp, cum = [0]*C, [0]*C
            for d in range(u, R):
                for i in range(C):
                    temp[i]+=matrix[d][i]
                    cum[i] = temp[i] + (cum[i-1] if i>0 else 0)
                # print(temp, cum)
                bs = []
                for i in range(C):
                    pos = bisect.bisect_left(bs, cum[i]-k)   # find a smallest cum[j] that >=cum[i]-k
                    if cum[i]<=k: ans = max(ans, cum[i])
                    if pos<len(bs):
                        ans = max(ans, cum[i]-bs[pos])
                        if ans==k: return ans
                    bs.insert(bisect.bisect(bs, cum[i]), cum[i])

        return ans