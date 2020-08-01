class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # 看不懂怎么bit操作的
        # 状态机 00->01->10->00，定义状态转换
        ones, twos = 0, 0
        for n in nums:
            ones = (ones^n)&~twos
            twos = (twos^n)&~ones
        return ones

        
        
