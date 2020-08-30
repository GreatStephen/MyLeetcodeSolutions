class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
            
        for i in range(len(arr)):
            if i-1+m*k>=len(arr):
                break
            pat = arr[i:i+m]
            count = k
            l, r = i, i+m-1
            for x in range(k):
                if arr[l:r+1]==pat:
                    count -= 1
                    l, r = l+m, r+m
                else: 
                    break
                
            if count==0:
                return True
        
        return False