class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        R,C = len(mat), len(mat[0])
        counti, countj = [0]*R, [0]*C
        
        for i in range(R):
            for j in range(C):
                num = mat[i][j]
                if num==0: continue
                counti[i] += 1
                countj[j] += 1
                    
        
        ans = 0
        for i in range(R):
            for j in range(C):
                num = mat[i][j]
                if num==0: continue
                if counti[i]==1 and countj[j]==1:
                    ans += 1
        return ans