class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        ans = 0
        for l in range(1, len(arr)+1, 2):            
            for i in range(len(arr)-l+1):
                j = i+l-1
                ans += sum(arr[i:j+1])
        return ans