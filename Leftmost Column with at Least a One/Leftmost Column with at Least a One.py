# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        # 正常方法是对每一行做BS，找到最左侧的1，在所有row中取最小的左侧1
        # 这个方法更巧妙，从右上角开始，碰到0往下走，碰到1往左走，这样下去一定会经过最左端的1
        # best case = O(min(R,c)), avg case = O(R+C)
        R,C = binaryMatrix.dimensions()
        i,j = 0, C-1
        ans = float('inf')
        
        while i<R and j>=0:
            if binaryMatrix.get(i,j)==1:
                ans = min(ans, j)
                j -= 1
            else:
                i += 1
        
        return ans if ans!=float('inf') else -1