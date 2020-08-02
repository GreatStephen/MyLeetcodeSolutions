class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        cur = max(arr[0], arr[1])
        count = 1
        for i in range(2, len(arr)):
            if count==k: return cur
            if cur>arr[i]:
                count+=1
            else:
                cur = arr[i]
                count = 1
            
        return cur