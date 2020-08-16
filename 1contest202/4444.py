class Solution(object):
    def minDays(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        def DFS(num, res):
            # ans = float('inf')
            if num==1:
                return 1+res
            if not num%3:
                return DFS(num/3, res+1)
            if not num&1:
                ans = DFS(num/2, res+1)
                ans = min(ans, DFS(num-1, res+1))
                return ans
            return DFS(num-1, res+1)
            
        
        return DFS(n, 0)