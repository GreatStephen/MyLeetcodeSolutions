class Solution:
    def getRow(self, k: int) -> List[int]:
        ans = [1]+[0]*k
        
        for i in range(k):
            temp = [0]+ans[:-1]
            for j in range(i+2):
                ans[j]+=temp[j]
        
        return ans