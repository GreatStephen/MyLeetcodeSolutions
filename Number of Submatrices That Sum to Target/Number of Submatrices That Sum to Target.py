class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        # 还是老方法，遍历所有行，对几行的合并算cum，然后用map在这个cum数组里找target
        R,C = len(matrix), len(matrix[0])
        
        # cumulative sum of each row
        cum = [[0]*C for _ in range(R)]
        for i in range(R):
            for j in range(C):
                if j==0: cum[i][j] = matrix[i][j]
                else: cum[i][j] = matrix[i][j]+cum[i][j-1]
        # print(cum)
        
        # for each submatrix, use dict to find target sum
        ans = 0
        for i in range(R):
            tempcum = [0]*C
            for l in range(1, R-i+1):
                for k in range(C):
                    tempcum[k]+=cum[i+l-1][k]
                # use map
                d = {0:1}
                for k in range(C):
                    tar = tempcum[k]-target
                    if tar in d: ans+=d[tar]
                    if tempcum[k] in d: d[tempcum[k]]+=1
                    else: d[tempcum[k]]=1
        return ans