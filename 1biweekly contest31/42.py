class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        dp = []
        for i,v in enumerate(target):
            if i==0: dp.append(v)
            else:
                if v<=target[i-1]: dp.append(dp[-1])
                else: dp.append(dp[-1]+v-target[i-1])
        
        return dp[-1]