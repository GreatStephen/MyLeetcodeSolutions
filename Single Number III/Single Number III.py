class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        X = reduce(lambda x, y: x^y, nums) # 所有数字的XOR，即为两个target的XOR
        offset = 0
        while not X&1:
            X>>=1
            offset += 1 # 找到右侧第一个1，统计右移多少位
        
        l0, l1 = [], [] # 以最右侧的1为标志，将nums分成两个组
        for n in nums:
            if (n>>offset)&1: l1.append(n)
            else: l0.append(n)
        
        # 两组分别XOR，即为两个结果
        ans = [reduce(lambda x,y: x^y, l0), reduce(lambda x,y: x^y, l1)]
        
        return ans