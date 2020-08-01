class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # 自己瞎写的, O(N) space
        d = {}
        for n in nums:
            if n not in d:
                d[n] = 2
            else:
                d[n] -=1
                if d[n]==0:
                    del d[n]
        print(d)
        for i,v in d.items():
            return i