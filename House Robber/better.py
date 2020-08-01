class Solution:
    def rob(self, nums: List[int]) -> int:
        # 一维dp，将数组优化成只有两个元素, p2->p1->n
        # p2记录i-2之前的最大值，p1记录i-1之前的最大值
        # 选n的话，就用p2+n。不选n的话，就取p1。两个数取最大值
        p1, p2 = 0, 0
        for n in nums:
            t = p1
            p1 = max(p1, p2+n)
            p2 = t
        return p1