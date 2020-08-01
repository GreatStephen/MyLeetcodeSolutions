class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        # 三维dp，dp[i][j][c]=以[i][j]为左上角，切c次，有几种结果
        # i,j逆序遍历，c从0到k-1
        # cum的作用是，计算upper或left part是否存在至少一个苹果
        R,C = len(pizza), len(pizza[0])
        dp = [[[0]*k for i in range(C)] for j in range(R)]
        # print(dp)
        
        # compute cum[][]
        cum = [[0]*(C+1) for _ in range(R+1)]
        for i in range(R-1, -1, -1):
            for j in range(C-1, -1, -1):
                cum[i][j] = cum[i+1][j]+cum[i][j+1]-cum[i+1][j+1]+(1 if pizza[i][j]=='A' else 0)
        # print(cum)
        
        for c in range(k):
            for i in range(R-1, -1, -1):
                for j in range(C-1, -1, -1):
                    val = 0
                    if c==0: # base case
                        if cum[i][j]>0:
                            dp[i][j][c]=1
                            continue
                    for rr in range(i+1, R): # cut horizontally
                        if cum[i][j]-cum[rr][j]>0: val+=dp[rr][j][c-1] # one apple should be in the upper part
                    for cc in range(j+1, C): # cur vertically
                        if cum[i][j]-cum[i][cc]>0: val+=dp[i][cc][c-1] # one apple should be in the left part
                    dp[i][j][c] = val
        
        return dp[0][0][-1]%(10**9+7)