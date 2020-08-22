class Solution(object):
    def differByOne(self, dict):
        # O(NM)，其实是把M^2拆成了两次循环
        hashvalue = []
        
        # 先计算所有单词的hash，26进制数字
        for d in dict:
            ans = 0
            for c in d:
                ans *= 26
                ans += ord(c)-97
            hashvalue.append(ans)
        
        # 这里有个技巧，外层循环是位数，内层循环才是单词，这样可以减少set的体积
        offset = 26**(len(dict[0])-1)
        for j in range(len(dict[0])):
            s = set()
            for i in range(len(dict)):
                h = hashvalue[i]
                newh = h-(ord(dict[i][j])-97)*offset # 每一个单词都减去第j位的值
                if newh in s: # 以此作为是否出现过的标志，而不是变成*星号
                    return True
                s.add(newh)
            offset /= 26
                
        return False
        