class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums)==1: return nums[0]
        l,r = 0, len(nums)-1
        mid = (l+r+1)//2
        if nums[l]<nums[r]: 
            return nums[l]
        elif nums[l]==nums[r]:
            return min(self.findMin(nums[l:mid]), self.findMin(nums[mid:r+1]))
        if nums[l]<=nums[mid]:
            return self.findMin(nums[mid+1:r+1])
        else:
            return self.findMin(nums[l+1:mid+1])