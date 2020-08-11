class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        # 这题不复杂啊，就两个串一一对应就好
        # 坑：s1的字符想要变成s2的对应字符，需要先变成一个s2中不存在的字符过渡。
        # 因为直接变的话，s1后面如果又出现这个字符，就会把前面已经变好的再次改变
        # 所以如果s2包含26个字符的话，是无论如何也没有解的
        if len(str1)!=len(str2): return False
        if str1==str2: return True
        d = {}
        for i,c1 in enumerate(str1):
            c2 = str2[i]
            if c1 not in d:
                d[c1] = c2
            elif d[c1]!=c2:
                return False
        
        if len(set(str2))<26:
            return True
        return False