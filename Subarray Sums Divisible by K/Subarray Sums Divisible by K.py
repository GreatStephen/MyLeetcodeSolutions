class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        cum, mod = [], []
        for i in range(len(A)):
            cum.append(A[i]+(cum[-1] if len(cum)>0 else 0))
            mod.append(cum[i]%K)
        mod.insert(0, 0)
        # print(cum, mod)
        
        d, ans = {}, 0
        for i in range(len(mod)):
            if mod[i] not in d:
                d[mod[i]] = 1
            else:
                ans += d[mod[i]]
                d[mod[i]] += 1
        
        return ans