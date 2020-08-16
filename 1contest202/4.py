class Solution(object):
    def minDays(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        def DFS(num, res):
            if not num:
                return res
            ans = float('inf')
            if not num%3:
                ans = min(ans, DFS(num/3, res+1))
            if not num&1:
                ans = min(ans, DFS(num/2, res+1))
            ans = min(ans, DFS(num-1, res+1))
            return ans
        
        
        
        
        return DFS(n, 0)


# 429