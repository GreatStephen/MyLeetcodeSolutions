class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        powers = set()
        for i in range(22):
            powers.add(2**i)
        # print(powers)
        
        seen = {}
        ans = 0
        for num in deliciousness:
            for p in powers:
                if p-num in seen:
                    ans += seen[p-num]
            if num not in seen:
                seen[num] = 0
            seen[num] += 1
        
        return ans%(10**9+7)