class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        ans = nums[0]+nums[1]+nums[2]
        nums.sort()
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l<r:
                sumval = nums[i]+nums[l]+nums[r]
                if abs(sumval-target) < abs(ans-target):
                    ans = sumval
                if sumval<target:
                    while l<r and nums[l]==nums[l+1]:
                        l+=1
                    l+=1
                elif sumval>target:
                    while l<r and nums[r]==nums[r-1]:
                        r-=1
                    r-=1
                else:
                    return ans
        return ans
