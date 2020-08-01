class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        # 三段式解决，以中间sub为基准，计算左sub的累计最大值，计算右sub的累计最大值
        # 然后对每个可能的midsub，将其加上对应的左最大值和右最大值，然后取最大即可
        # mid范围[k,n-2k]，left范围[0,n-2k-1]，right范围[2k,ending]
        N = len(nums)
        left, right, mid, cum = [None]*N, [None]*N, [None]*N, []
        
        # cum[]
        for i in range(len(nums)):
            if i==0: cum.append(nums[i])
            else: cum.append(cum[-1]+nums[i])
        
        # left max subsum
        for i in range(k, N-2*k+1): # [k, N-2k] inclusive
            if i==k: 
                left[i] = (cum[i-1], 0)
            else:
                subsum = cum[i-1]-cum[i-1-k]
                if subsum>left[i-1][0]:
                    left[i] = (subsum, i-k)
                else:
                    left[i] = tuple(left[i-1])
        
        # right max subsum
        for i in range(N-2*k, k-1, -1):
            if i==(N-2*k):
                right[i] = (cum[-1]-cum[i+k-1], N-k)
            else:
                subsum = cum[i+2*k-1]-cum[i+k-1]
                if subsum>=right[i+1][0]:
                    right[i] = (subsum, i+k)
                else:
                    right[i] = tuple(right[i+1])
        
        # print(left, right)
        
        # mid
        MAX, ans = 0, []
        for i in range(k, N-2*k+1):
            midsum = cum[i+k-1]-cum[i-1]
            if midsum+left[i][0]+right[i][0]>MAX:
                ans = [left[i][1], i, right[i][1]]
                MAX = midsum+left[i][0]+right[i][0]
        
        return ans