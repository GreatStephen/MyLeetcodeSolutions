class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = []
        s = 0
        for n in nums:
            s += n
            ans.append(s)
        
        return ans