class Solution:
    def closestToTarget(self, arr: List[int], target: int) -> int:
        andarr = [arr[-1]]
        ans = abs(andarr[0]-target)
        
        for l in range(len(arr)-2, -1, -1):
            for i in range(len(andarr)):
                andarr[i] &= arr[l]
            andarr.append(arr[l])
            pos = bisect.bisect_left(andarr, target)
            if pos<len(andarr): ans = min(ans, abs(andarr[pos]-target))
            if pos>0: ans = min(ans, abs(andarr[pos-1]-target))
            
        return ans