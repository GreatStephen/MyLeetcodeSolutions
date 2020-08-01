# take my heart with you
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums)<2: return False
        d = collections.defaultdict(int)
        sum = 0
        if k ==0:   # edge case
            if any(nums[i]==nums[i-1]==0 for i in range(1,len(nums))): return True
            else: return False
        for i in range(len(nums)):
            sum += nums[i]
            mod = sum%k 
            if mod==0 and i>0: return True
            if mod in d and d[mod] < i-1: return True
            if mod not in d: d[mod] = i
        return False
                