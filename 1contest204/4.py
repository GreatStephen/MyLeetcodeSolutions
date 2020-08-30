class Solution:
    # def factorial(self, num):
    #     ans = 1
    #     for i in range(1, num+1):
    #         ans *= i
    #     return ans%(10**9+7)
    
    def numOfWays(self, nums: List[int]) -> int:
        def factorial(num):
            ans = 1
            for i in range(1, num+1):
                ans *= i
            return ans%(10**9+7)
        def C(m,n):
            n = min(n, m-n)
            if n==0:
                return 1
            ans = 1
            cur = m
            for i in range(1, n+1):
                ans *= cur
                cur -=  1
            ans /= factorial(n)
            return int(ans%(10**9+7))
        def partition(m,n):
            if n==1: return 1
            return C(m-1,n-1)
            
        def helper(nums):
            if not nums:
                return 1
            smaller, larger = [], []
            MOD = 10**9+7
            ans = 0
            for i in range(1, len(nums)):
                if nums[i]>nums[0]:
                    larger.append(nums[i])
                else:
                    smaller.append(nums[i])
            # print(smaller, larger)
            if not smaller:
                return helper(larger)
            if not larger:
                return helper(smaller)
            num1, num2 = helper(smaller), helper(larger)
            # print(num1, num2)

            len1, len2 = max(len(smaller), len(larger)), min(len(smaller), len(larger))
            # print(len1, len2, num1, num2)
            temp = 0
            for x in range(1, len2+1):
                # print(len1, len2, partition(len2,x))
                temp += C(len1+1, x)*partition(len2,x)
            return (temp*num1*num2)%MOD
        
        return int(helper(nums)-1)
            
            