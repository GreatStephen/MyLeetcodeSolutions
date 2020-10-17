class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        
        l = len(arr)/20
        # print(l)
        l = int(l)
        
        temp = 0
        for i in range(l):
            temp += arr[i]
        for i in range(len(arr)-l, len(arr)):
            temp += arr[i]
        
        # print(len(arr)-l*2)
        ans = (sum(arr)-temp)/(len(arr)-l*2)
        return ans
                
        
        
        