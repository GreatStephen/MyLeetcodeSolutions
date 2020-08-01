class Solution:
    def minFlips(self, target: str) -> int:
        dp, ans = [int(target[0])], 0
        
        for i,v in enumerate(target):
            if i==0: continue
            dp.append(dp[-1] + (int(target[i-1])^int(v)))
        
        # print(dp)
        return dp[-1]