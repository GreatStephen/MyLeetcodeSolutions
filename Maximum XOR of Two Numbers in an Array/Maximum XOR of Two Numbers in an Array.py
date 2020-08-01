class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        # Stefan推荐的方法，bit by bit，速度快一些, trie速度相对较慢
        ans = 0
        mask = 0
        for i in range(31, -1, -1):
            # bit by bit构建ans，从最高位开始，检查每个bit能否成为1
            mask |= (1<<i)
            s = set()
            for n in nums:
                s.add(n&mask)   # 先把每个数字都只取前mask位
            target = (ans | (1<<i)) # target是第i位变成1的数字，是希望得到的结果
            for n in s:
                if n^target in s: # a^b=c和a^c=b相等，检查是否存在s中两个数字a,b，使a^b=target，只需要检查a^target是否在s中即可
                    ans = target
                    break
        return ans