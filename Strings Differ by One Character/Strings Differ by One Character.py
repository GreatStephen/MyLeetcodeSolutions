class Solution(object):
    def differByOne(self, dict):
        # O(NM^2)，把每个字符的每个位置换成'*'，然后判断这个带星的字符是否出现过
        s = set()
        for d in dict:
            for i in range(len(d)):
                temp = d[:i]+'*'+d[i+1:]
                if temp in s:
                    return True
                s.add(temp)
        return False
        