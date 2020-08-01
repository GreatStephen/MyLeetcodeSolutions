class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        mid = (l+r)//2
        if l==r:
            return nums[l]
        if nums[0]>nums[-1]:
            if nums[mid]>=nums[0]:
                return self.findMin(nums[mid+1:])
            else:
                return self.findMin(nums[:mid+1])
        else:
            return nums[0]
        
    
        