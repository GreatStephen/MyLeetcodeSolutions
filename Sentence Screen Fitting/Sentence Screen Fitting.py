class Solution(object):
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        # 记录下每一行以下标为i的单词开头时，这一行能放多少个words
        d = {}
        for i,s in enumerate(sentence):
            idx, j = 0, i
            num = 0
            while idx<cols: # 这个地方可以优化，不需要用j进行二次遍历，可以用滑窗记录l,r一共多少个单词
                idx += len(sentence[j]) # 每次让j从i开始往右遍历太慢了，如果每个word很短，j需要大量移动
                j = (j+1)%len(sentence)
                if idx<=cols: num+=1
                else: break
                idx += 1
            d[i] = num
        # print d
        
        idx, ans = 0, 0
        for r in xrange(rows):
            idx += d[idx]
            if idx>=len(sentence):
                ans += idx/len(sentence)
                idx %= len(sentence)
        return ans