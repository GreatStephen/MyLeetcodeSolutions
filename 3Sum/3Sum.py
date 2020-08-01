class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        
        for i,n in enumerate(nums):
            if n>0: break
            if i>=len(nums)-2: break
            if i>0 and n==nums[i-1]: continue
            l,r = i+1, len(nums)-1
            while l<r:
                s = nums[l]+nums[r]
                if s+n==0:
                    ans.append([n, nums[l], nums[r]])
                    l+=1
                    r-=1
                elif s+n<0:
                    l+=1
                elif s+n>0:
                    r-=1
                while i+1<l<len(nums)-1 and nums[l]==nums[l-1]: l+=1
                while i+1<r<len(nums)-1 and nums[r]==nums[r+1]: r-=1
        return ans