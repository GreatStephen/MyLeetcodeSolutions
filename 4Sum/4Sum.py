class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums)<4:
            return []
        ans = []
        nums.sort()
        for i in range(0, len(nums)-3):
            if i>0 and nums[i]==nums[i-1]:
                continue
            if 4*nums[i] > target:
                break
            ans.extend(self.threeSum(nums, i+1, target-nums[i], nums[i]))
        return ans


    def threeSum(self, nums: List[int], start: int, target: int, first_num: int) -> List[List[int]]:
        # ans = nums[0]+nums[1]+nums[2]
        # nums.sort()
        ans = []
        for i in range(start, len(nums)-2):
            if i>start and nums[i]==nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l<r:
                sumval = nums[i]+nums[l]+nums[r]
                if sumval<target:
                    while l<r and nums[l]==nums[l+1]:
                        l+=1
                    l+=1
                elif sumval>target:
                    while l<r and nums[r]==nums[r-1]:
                        r-=1
                    r-=1
                else:
                    lst = []
                    lst.extend([first_num,nums[i],nums[l],nums[r]])
                    ans.append(lst)
                    while l<r and nums[l]==nums[l+1]:
                        l+=1
                    l+=1
                    while l<r and nums[r]==nums[r-1]:
                        r-=1
                    r-=1
        return ans