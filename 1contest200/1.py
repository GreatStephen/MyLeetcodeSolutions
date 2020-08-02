class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        N = len(arr)
        ans = 0
        
        for i in range(N-2):
            for j in range(i+1, N-1):
                if abs(arr[i]-arr[j])>a: continue
                for k in range(j+1, N):
                    if abs(arr[j]-arr[k])>b: continue
                    if abs(arr[i]-arr[k])>c: continue
                    ans += 1
        
        return ans