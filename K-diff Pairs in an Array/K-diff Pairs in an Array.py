class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        # counter是个好东西。要是java就得用hashmap
        ct = Counter(nums)
        ans = 0
        for num in ct.keys():
            if k==0:
                if ct[num]>=2: ans += 1
            else:
                if ct[num+k]>0: ans += 1
        return ans