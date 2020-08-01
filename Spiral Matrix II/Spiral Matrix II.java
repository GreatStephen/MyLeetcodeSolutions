class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        i_offset = [0, 1, 0, -1]
        j_offset = [1, 0, -1, 0]
        val, i, j, offset_idx = 1, 0, 0, 0
        ans = [[0 for x in range(n)] for y in range(n)]
        while(val<=n*n):
            ans[i][j] = val
            val+=1
            new_i, new_j = i+i_offset[offset_idx], j+j_offset[offset_idx]
            if new_i<0 or new_i>=n or new_j<0 or new_j>=n or ans[new_i][new_j]!=0:
                offset_idx = (offset_idx+1)%4
                new_i, new_j = i+i_offset[offset_idx], j+j_offset[offset_idx]
            # print(new_i, new_j)
            i, j = new_i, new_j
        
        return ans