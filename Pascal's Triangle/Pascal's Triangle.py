class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==0:
            return []
        ans = [[1]]
        for i in range(1, numRows):
            ans.append(list(map(lambda x,y: x+y, [0]+ans[-1], ans[-1]+[0])))
        return ans