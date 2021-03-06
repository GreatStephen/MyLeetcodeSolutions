class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def helper(arr):
            if len(arr)==1: return True
            diff = arr[1]-arr[0]
            for i in range(1, len(arr)):
                if arr[i]-arr[i-1]!=diff:
                    return False
            return True
        
        ans = []
        for i in range(len(l)):
            ans.append(helper(sorted(nums[l[i]: r[i]+1])))
        return ans