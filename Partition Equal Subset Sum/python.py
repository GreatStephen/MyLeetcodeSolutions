class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s&1: return False
        s //= 2
        
        dp = [True]+[False]*s
        
        # 本质：看能否用nums里的数字组成sum这个和
        # 每拿一个数字进来，之前所有可能结果加上n，都改为true。最后看看dp[-1]是否true。
        for n in nums:
            temp = dp[:]
            for i in range(s-n+1):
                if dp[i]:
                    temp[i+n] = True
            dp = temp
        
        return dp[-1]