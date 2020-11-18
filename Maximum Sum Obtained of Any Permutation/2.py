class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        count = [0]*(len(nums)+1)
        for s,e in requests:
            count[s] += 1
            count[e+1] -= 1
        cum = 0
        for i,c in enumerate(count):
            cum += c
            count[i] = cum
        
        ans = 0
        for n,freq in zip(sorted(nums), sorted(count[:-1])):
            ans += n*freq
        return ans%(10**9+7)
                