class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        # 2维dp仍然超时
        ans, MOD = 0, 10**9+7
        dp = [[0]*len(arr) for _ in range(len(arr))]
        
        for l in range(1, len(arr)+1):
            for i in range(len(arr)-l+1):
                j = i+l-1
                # print(i,j)
                if i==j:
                    flag = arr[i]&1 
                    # print(flag)
                else:
                    flag = (dp[i][j-1])^(arr[j]&1)
                dp[i][j] = flag
                ans += flag   
        
        
        
        # print(dp)
        return ans%MOD