class Solution(object):
    def minOperations(self, nums):
        self.ans = 0
        def helper(nums):
            allzero = True
            for i,n in enumerate(nums):
                if n&1:
                    nums[i] -= 1
                    self.ans += 1
                    even = False
                if nums[i]>0:
                    allzero = False
            if allzero:
                return
            self.ans += 1
            for i in range(len(nums)):
                nums[i] /= 2
                    
        
        while sum(nums):
            helper(nums)
        return self.ans