class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        ans = 0
        def helper(l,r):
            # print(l,r)
            if l>r: return 0
            neg_count = 0
            idx = [l-1,None]
            ans = 0
            for i in range(l, r+1):
                if nums[i]<0:
                    neg_count += 1
                    neg_count %= 2
                # print(neg_count)
                if idx[neg_count]==None:
                    idx[neg_count] = i
                else:
                    ans = max(ans, i-idx[neg_count])
                # print(idx)
            # print(ans)
            return ans
        
        
        
        last_zero = -1
        for i in range(len(nums)):
            if nums[i]==0:
                ans = max(ans, helper(last_zero+1, i-1))
                last_zero = i
        # if last_zero<0:
        ans = max(ans, helper(last_zero+1, len(nums)-1))
        return ans