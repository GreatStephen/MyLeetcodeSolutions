class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        for n in nums:
            if nums[abs(n)-1]<0:
                ans.append(abs(n))
            else:
                nums[abs(n)-1]*=-1
        return ans