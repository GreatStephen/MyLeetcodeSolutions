class Solution:
    def specialArray(self, nums: List[int]) -> int:
        for x in range(len(nums)+1):
            a = reduce(lambda n1,n2: n1+1 if n2>=x else n1, nums, 0)
            if x==a:
                return x
        
        return -1