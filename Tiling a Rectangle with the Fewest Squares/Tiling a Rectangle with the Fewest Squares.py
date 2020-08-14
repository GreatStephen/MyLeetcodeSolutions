class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        if n==m: return 1
        if m>n:
            m,n = n,m        
        
        # greedy+DP, 找到最低最左的位置，以这个位置填入所有合格的正方形，然后递归
        @lru_cache(None)
        def helper(skyline):
            if all(h==n for h in skyline):
                return 0
            
            ans = float('inf')
            minh = min(skyline)
            l = skyline.index(minh)
            for r in range(l,m):
                if skyline[r]!=minh: break
                if r-l+1>n-minh: break
                newsl = list(skyline)
                for i in range(l,r+1):
                    newsl[i]+=r-l+1
                ans = min(ans, helper(tuple(newsl)))
            return ans+1        
        
        ans = helper(tuple([0]*m)) # initial skyline
        return ans