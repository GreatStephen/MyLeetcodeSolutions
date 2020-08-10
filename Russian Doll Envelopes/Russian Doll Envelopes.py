class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes or not envelopes[0]:
            return 0
        # 按[0]升序，按[1]降序排列。然后只对[1]做300.LIS即可
        # 对[1]降序保证了当[0]相同时，后面的不可能与前面的连在一起，因为后面的[1]必定比前面的小
        # 这道题两个相同的数字是不能套在一起的，所以[1]降序保证了相同的[0]里面只会选择一个[1]最小且合格的[1]
        envelopes = sorted(envelopes, key = lambda x: (x[0], -x[1]))
        N = list(zip(*envelopes))[1]
        
        # LIS
        dp = []
        for n in N:
            pos = bisect.bisect_left(dp, n)
            if pos==len(dp):
                dp.append(n)
            else:
                dp[pos] = n
        return len(dp)