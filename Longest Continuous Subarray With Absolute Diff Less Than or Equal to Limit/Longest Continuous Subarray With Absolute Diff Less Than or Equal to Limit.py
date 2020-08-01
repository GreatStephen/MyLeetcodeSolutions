class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # maxd是递减序列，存放最大值，mind是递增序列，存放最小值
        # maxd[0]和mind[0]永远是当前window中的最大最小值
        # 将l不断右移，如果nums[l]等于最大或最小值，将其抛出
        maxd, mind = deque(), deque()
        l=0
        ans = 0
        for r,n in enumerate(nums):
            while maxd and maxd[-1]<n:
                maxd.pop()
            maxd.append(n)
            while mind and mind[-1]>n:
                mind.pop()
            mind.append(n)

            # shrink l
            while maxd[0]-mind[0]>limit:
                if maxd[0]==nums[l]:
                    maxd.popleft()
                if mind[0]==nums[l]:
                    mind.popleft()
                l+=1
            ans = max(ans, r-l+1)
        
        return ans
            