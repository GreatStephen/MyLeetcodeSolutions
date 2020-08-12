class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        # backtracking/DFS
        s = sum(nums)
        if s%k: return False
        s /= k
        if max(nums)>s: return False
        visited = [0]*len(nums)
        
        # 尝试所有的数字组合，如果有一个组合=sum，那么下一次递归就让k-1
        # 就是一个常规的DFS backtracking
        def DFS(start_idx, cur_sum, k):
            if k==0: return True
            if cur_sum==s:
                return DFS(0, 0, k-1)
            for i in range(start_idx, len(nums)):
                n = nums[i]
                if visited[i]==1: continue
                if cur_sum+n<=s:
                    visited[i]=1
                    if DFS(i+1, cur_sum+n, k): return True
                    visited[i]=0
            return False
        
        return DFS(0,0,k)