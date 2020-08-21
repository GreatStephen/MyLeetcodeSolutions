class Solution(object):
    def candyCrush(self, board):
        # 对每一个board值的abs，往右和往下检查是否3个以上相同。如果是，就全变成负数
        R,C = len(board), len(board[0])
        def crush():
            ans = False
            for i in range(R):
                for j in range(C):
                    if board[i][j]==0:
                        continue
                    num = abs(board[i][j])
                    count, k = 1, j+1
                    while k<C and abs(board[i][k])==num:
                        k += 1
                        count += 1
                    if count>=3:
                        ans = True
                        for k in xrange(j,j+count):
                            board[i][k] = -num
                            # board[i][k] = 0
                    count, k = 1, i+1
                    while k<R and abs(board[k][j])==num:
                        k += 1
                        count += 1
                    if count>=3:
                        ans = True
                        for k in xrange(i,i+count):
                            board[k][j] = -num
            return ans
        
        # 对于负数和其他的0，沉降
        def resize():
            for c in range(C):
                l,r = R-1, R-1
                while r>=0:
                    while r>=0 and board[r][c]<=0:
                        r -= 1
                    if r<0: break
                    board[l][c] = board[r][c]
                    l -= 1
                    r -= 1
                while l>=0:
                    board[l][c] = 0
                    l -= 1
        
        
        while crush():
            resize()
        return board