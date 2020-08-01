class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if len(nums)==0: return []
        nums.sort()
        # prev用来记录最长路径上的前一个节点，顺着这个链接往前寻找，即可找到最长的链路
        dp, prev = [1]*len(nums), [None]*len(nums)
        ans_idx, max = 0, 0
        for i in range(len(nums)):
            for j in range(i-1, -1, -1):
                if nums[i]%nums[j]==0 and dp[j]+1>dp[i]:
                    dp[i] = dp[j]+1
                    prev[i] = j
                    if dp[i]>max:
                        max = dp[i]
                        ans_idx = i
        
        ans = set()
        while ans_idx!=None:
            ans.add(nums[ans_idx])
            ans_idx = prev[ans_idx]
        
        return ans