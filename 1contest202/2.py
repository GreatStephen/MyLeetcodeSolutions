class Solution(object):
    def minOperations(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n&1:
            return (n/2)*(1+n/2)
        else:
            # return (1+2*(n/2))*(n/2)/2
            return (n/2)*(n/2)