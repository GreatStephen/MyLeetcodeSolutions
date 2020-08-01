class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        R,C = len(mat), len(mat[0])
        cum = [[0]*(C+1) for _ in range(R+1)]
        
        for i in range(1, R+1):
            for j in range(1, C+1):
                cum[i][j] = cum[i-1][j]+cum[i][j-1]-cum[i-1][j-1]+mat[i-1][j-1]
        # print(cum)
        
        ans = [[0]*C for _ in range(R)]
        for i in range(R):
            for j in range(C):
                tl, br = [i,j], [i,j] # 找到正确的左上角和右下角
                for k in range(K):
                    if tl[0]-1>=0: tl[0]-=1
                    else: break
                for k in range(K):
                    if tl[1]-1>=0: tl[1]-=1
                    else: break
                for k in range(K):
                    if br[0]+1<R: br[0]+=1
                    else: break
                for k in range(K):
                    if br[1]+1<C: br[1]+=1
                    else: break
                # 通过左上角和右下角和cum，计算小矩形的和
                ans[i][j] = cum[br[0]+1][br[1]+1]-cum[tl[0]][br[1]+1]-cum[br[0]+1][tl[1]]+cum[tl[0]][tl[1]]
        return ans