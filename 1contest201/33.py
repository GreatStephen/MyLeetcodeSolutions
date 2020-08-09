class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        ans = 0
        cum = 0
        s = {0}
        
        for j,n in enumerate(nums):
            cum += n
            if cum-target in s :
                ans += 1
                cum = 0
                s = {0}
            
            else:
                s.add(cum)
        
        return ans
                
                