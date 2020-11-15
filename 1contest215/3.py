class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        l, r = 0, len(nums)-1
        while x>=0 and r>=l:
            x -= nums[r]
            r -= 1
        if r<0 and x>0:
            return -1
        elif r<0 and  x==0:
            return len(nums)
        
        # print(l,r)
        ans = float('inf')
        while r<len(nums):
            # print(l,r)
            while x<=0 and r+1<len(nums):
                if x==0:
                    ans = min(ans, len(nums)-(r-l+1))
                x += nums[r+1]
                r += 1
            if r+1>=len(nums):
                if x==0:
                    ans = min(ans, len(nums)-(r-l+1))
                break
            while x>=0:
                if x==0:
                    ans = min(ans, len(nums)-(r-l+1))
                x -= nums[l]
                l += 1
        
        return ans if ans!=float('inf') else -1