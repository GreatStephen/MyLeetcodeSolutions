class Solution:
    # 用数字代表概率，同时记录下sum和cum[]数组
    def __init__(self, nums: List[int]):
        self.prob = []
        for n in nums:
            self.prob.append((self.prob or [0])[-1] + n)
        self.s = self.prob[-1]

    def pickIndex(self) -> int:
        # 产生[0:sum-1]的随机数，用右侧对齐binary search找到下标
        ran = random.randint(0, self.s-1)
        pos = bisect.bisect(self.prob, ran)
        
        return pos


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()