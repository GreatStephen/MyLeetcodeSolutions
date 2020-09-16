class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        # 从左找出递增序列，从右找出递增序列
        # 对这两个序列做sliding window，看看r-l-1什么时候能达到最小
        left = 0
        while left+1<len(arr) and arr[left+1]>=arr[left]:
            left += 1
        right = len(arr)-1
        while right-1>left and arr[right-1]<=arr[right]:
            right -= 1
        ans = min(right, len(arr)-left-1)
        
        # a window
        l, r = 0, right
        while l<=left and l<r and r<len(arr):
            if arr[l]<=arr[r]:
                ans = min(ans, r-l-1)
                l += 1
            else:
                r += 1
        
        return ans
            