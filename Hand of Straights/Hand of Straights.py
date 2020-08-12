class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        if len(hand)%W: return False
        c = Counter(hand)
        # 统计每个数字的次数，再从小到大排列
        # 对于当前最小的数字i，应该存在以i为底长度为W的序列。统计所有这样的序列。
        
        for i in sorted(c):
            # 这里很巧妙，因为最小数字i的出现次数可能不止一次，所以对i,i+1,i+2...i+W-1，他们都要减去c[i]i的出现次数。
            # 如果发现某次减去i的出现次数之后，结果为负数，说明这个数组无法组成，false
            if c[i]>0:
                for j in range(1,W):
                    c[i+j]-=c[i]
                    if c[i+j]<0: return False
                c[i]=0
        
        return True