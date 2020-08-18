class Solution(object):
    def distributeCandies(self, candies, num_people):
        """
        :type candies: int
        :type num_people: int
        :rtype: List[int]
        """
        ans = [0] * num_people
        
        count, idx = 1, 0
        while candies>0:
            if count>=candies:
                ans[idx] += candies
                candies = 0
                continue
            ans[idx]+=count
            candies -= count
            count += 1
            idx = (idx+1)%num_people
            
        
        
        return ans