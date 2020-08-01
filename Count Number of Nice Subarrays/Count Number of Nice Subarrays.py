class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # 计算atMost()是个好方法，O(N)，两次就是O(N+N)，遍历两次所以慢一些，但逻辑简单
        def atMost(nums,k):
            l = ans = 0
            for r in range(len(nums)):
                if nums[r]&1: k -= 1
                while k<0:
                    if nums[l]&1: k += 1
                    l += 1
                ans += r-l+1
            return ans
        return atMost(nums, k)-atMost(nums, k-1)