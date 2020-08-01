class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        cnt = [0]*k
        for a in arr:
            if a<0:
                print((a%k+k)%k)
        
        return False