class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # 正常的滑动窗口，只遍历一次，所以速度正常
        r = l = res = count = 0
        for r in range(len(nums)):
            if nums[r]&1: k-=1
            if k==0:
                count = 0
                while k==0:
                    k += nums[l]&1
                    count += 1
                    l += 1
            res += count
        return res
                