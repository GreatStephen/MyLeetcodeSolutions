class Solution(object):
    def maximizeSweetness(self, sweetness, K):
        """
        :type sweetness: List[int]
        :type K: int
        :rtype: int
        """
        
        lo, hi = min(sweetness), sum(sweetness)/(K+1)
        # print(lo, hi)
        
        # 把mid作为最小数字进行分割，看能把s分割成几段。如果分割的段数>=(K+1)，说明mid还可以再提高
        # 反之，如果分不出(K+1)段，说明mid太大了
        # BS很巧妙
        ans = 0
        while lo<=hi:
            mid = (lo+hi)/2
            cur, cnt = 0, 0
            for s in sweetness:
                cur += s
                if cur>=mid:
                    cnt += 1
                    cur = 0
            if cnt>=(K+1):
                ans = max(ans, mid)
                lo = mid+1
            else:
                hi = mid-1
        
        return ans