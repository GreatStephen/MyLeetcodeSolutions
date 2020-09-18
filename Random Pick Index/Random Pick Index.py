class Solution:
    # reservoir sampling，概率问题。对于n长度的数组来说，n未知，但我想用相等的概率从n里面取一个
    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        ans = -1
        count = 0
        for i in range(len(self.nums)):
            if self.nums[i]==target:
                count += 1
                if random.randint(1,count)==1: # p=1/count的概率选择当前的帽子
                    ans = i
        return ans


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)