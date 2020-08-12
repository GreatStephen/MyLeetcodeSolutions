class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums)%k: return False
        c = Counter(nums)
        # print(c)
        
        for i in sorted(c):
            # print(i)
            if c[i]>0:
                for j in range(1,k):
                    c[i+j]-=c[i]
                    if c[i+j]<0: return False
                c[i]=0
        
        return True