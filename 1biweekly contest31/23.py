class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        # 一维dp终于过了
        ans, MOD = 0, 10**9+7
        dp = []
        s = []
        
        for i,v in enumerate(arr):
            if i==0: 
                dp.append(arr[i]&1)
                s.append(dp[-1])
            else:
                if arr[i]&1:
                    dp.append(i-dp[-1]+1)
                else:
                    dp.append(dp[-1])
                s.append(dp[-1]+s[-1])
        
        
        
        return s[-1]%MOD