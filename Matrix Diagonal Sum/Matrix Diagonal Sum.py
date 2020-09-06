class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        ans = 0
        R,C = len(mat), len(mat[0])
        idx1, idx2 = 0, R-1
        
        for j in range(C):
            if idx1==idx2:
                ans += mat[idx1][j]
            else:
                ans += mat[idx1][j]
                ans += mat[idx2][j]
            idx1 += 1
            idx2 -= 1
        return ans