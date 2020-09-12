class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # 这题是个简单的DFS+backtracking
        if k==1: return [[n]]
        def DFS(cur, k, n):
            if n<=0:
                return []
            if k==1:
                if n>cur[-1] and n<10:
                    return [cur+[n]]
                else:
                    return []
            ans = []
            for i in range(cur[-1]+1, 10):
                ans += DFS(cur+[i], k-1, n-i)
            return ans
        
        
        ans = []
        for i in range(1, 10):
            ans += DFS([i], k-1, n-i)
        return ans    
        