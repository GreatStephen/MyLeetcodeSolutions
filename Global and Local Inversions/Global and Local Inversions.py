class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        # 根据题目描述，只允许a[i]>a[i+1]，对于i+2之后的所有数字，必须全部大于a[i]
        # 基于此，每个a[i]实际上只允许存在于a[i-1]/a[i]/a[i+1]三个位置
        # 因此，检查a[i]-i是否等于-1/0/1即可
        for i,a in enumerate(A):
            if a-i not in [-1,0,1]:
                return False
        return True