class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        # for a diagonal, (i-j) is a constant
        R, C = len(mat), len(mat[0])
        offset = C-1
        l = [[] for i in range(R+C-1)]
        for i in range(R):
            for j in range(C):
                l[i-j+offset].append(mat[i][j])
        
        for row in l: row.sort()
        
        for i in range(R):
            for j in range(C):
                mat[i][j] = l[i-j+offset][0]
                l[i-j+offset].pop(0)
        return mat