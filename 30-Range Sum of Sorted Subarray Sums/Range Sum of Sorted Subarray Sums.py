class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        sumtozero = []
        for i,v in enumerate(nums):
            if i==0: sumtozero.append(nums[i])
            else: sumtozero.append(sumtozero[-1]+nums[i])
            
        sums = []
        for k in range(n):
            for i in range(n-k):
                j = i+k
                new_num = sumtozero[j]-(sumtozero[i-1] if i-1>=0 else 0)
                sums.append(new_num)
        sums.sort()
        
        ans = 0
        MOD = 10**9+7
        for i in range(left-1, right):
            ans += sums[i]
            ans %= MOD
        
        return ans
                