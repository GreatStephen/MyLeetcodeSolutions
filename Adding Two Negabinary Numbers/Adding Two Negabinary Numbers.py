class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # 看不懂，不知道为什么
        res, carry = [], 0
        while arr1 or arr2 or carry:
            carry += (arr1 or [0]).pop() + (arr2 or [0]).pop()
            res.append(carry&1)
            carry = -(carry>>1)
        
        # print(res)
        while len(res)>1 and res[-1]==0: res.pop()
        
        return res[::-1]
    