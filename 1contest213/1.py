class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        d = {}
        for p in pieces:
            d[p[0]] = p
        
        index = 0
        while index<len(arr):
            if arr[index] not in d:
                return False
            l = d[arr[index]]
            for i in range(len(l)):
                if l[i]!=arr[index]:
                    return False
                index += 1
        
        return True