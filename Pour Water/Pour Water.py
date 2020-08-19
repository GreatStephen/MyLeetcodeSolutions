class Solution(object):
    def pourWater(self, heights, V, K):
        """
        :type heights: List[int]
        :type V: int
        :type K: int
        :rtype: List[int]
        """

        # 这题是个智力题啊，没什么算法可言
        # 先往左走到走不了为止，然后往右走到走不了为止，再往左走到K为止。最后cur停下的位置就是雨水的位置
        # 就这样，想想就能想通
        for _ in xrange(V):
            cur = K
            while cur>0 and heights[cur-1]<=heights[cur]:
                cur -= 1
            while cur<len(heights)-1 and heights[cur+1]<=heights[cur]:
                cur += 1
            while cur>K and heights[cur-1]<=heights[cur]:
                cur -= 1
            heights[cur] += 1
            
            
        return heights