class Solution(object):
    def minDays(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 这个是错的
        ans = 0
        while n>0:
            if not n%3:
                n = n/3
                ans += 1
            elif not n&1 and not (n/2)&1:
                n = n/2
                ans += 1
            elif not n&1:
                if not (n-1)%3:
                    n -= 1
                    ans += 1
                else:
                    n = n/2
                    ans += 1
            else:
                n -= 1
                ans += 1
        
        return ans