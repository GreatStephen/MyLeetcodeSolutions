class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        # 本题的特殊点：如果字母c出现多次，那么以c结尾的连串只取最长的，因为连串的内容都是固定的
        # 为每个字母设一个数值，记录以这个字母为结尾的最长连串，也就是以这个字母结尾的子串数量
        # 从头遍历，遇到连串l+1，并记录给这个字母的max()。非连串则l=1，从1开始重新计算
        l, s = 1, [0]*26
        d = defaultdict()
        for c in "abcdefghijklmnopqrstuvwxyz":
            d[c] = (ord(c)-ord('a'))
        for i,c in enumerate(p):
            if i==0: s[d[c]] = 1
            else:
                if (d[p[i-1]]+1)%26 == d[c]:
                    l += 1                    
                else:
                    l = 1
                s[d[c]] = max(s[d[c]], l)
        
        return sum(s)