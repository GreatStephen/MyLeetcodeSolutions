class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # 记录0比1多多少个。如果当前0比1多x个，并且之前也在某个idx处0比1多x个，那么i,j之间一定0和1个数相等
        # 而且如果x已经在d里存在，就不需要更新，因为我们只需要最靠左的下标，能产生最长的串
        d = {0:-1}
        num0, num1 = 0, 0
        ans = 0
        for i,n in enumerate(nums):
            if n:
                num1 += 1
            else:
                num0 += 1
            if num0-num1 in d:
                ans = max(ans, i-d[num0-num1])
            else:
                d[num0-num1] = i
        return ans