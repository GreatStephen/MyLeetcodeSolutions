class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        ct = Counter(arr)
        
        ans = 0
        for freq in sorted(ct.values()):
            k -= freq
            if k>=0:
                ans += 1
            else:
                break
        
        return len(ct)-ans