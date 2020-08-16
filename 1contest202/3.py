class Solution(object):
    def maxDistance(self, position, m):
        """
        :type position: List[int]
        :type m: int
        :rtype: int
        """
        position.sort()
        # print position
        
        lo, hi = 1, (position[-1]-position[0])/(m-1)
        # print lo, hi
        
        
        def canPut(dis):
            num, lastpos = m, float('-inf')
            for p in position:
                if p-lastpos>=dis:
                    num -= 1
                    lastpos = p
                if not num:
                    break
            if not num:
                return True
            return False
            
        
        ans = 0
        while lo<=hi:
            mid = (lo+hi)/2
            if canPut(mid):
                ans = max(ans, mid)
                lo = mid+1
            else:
                hi = mid-1
        
        return ans
            
            
            