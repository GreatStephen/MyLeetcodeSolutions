class Solution:
    def countArrangement(self, N: int) -> int:
        # 普通的DFS
        def DFS(idx, nums):
            if idx==N:
                num = 0
                for n in nums: num = n
                if num%idx==0 or idx%num==0: return 1
                else: return 0
            ans = 0
            for num in list(nums):
                if num%idx==0 or idx%num==0:
                    nums.remove(num)
                    ans += DFS(idx+1, nums)
                    nums.add(num)
            return ans
        
        
        return DFS(1, set([i for i in range(1, N+1)]))