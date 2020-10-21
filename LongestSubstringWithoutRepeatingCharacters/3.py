class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = Max = 0
        d = {}
# 这道题妙在，d只存放每个字母的最右距离即可。
# 当start小于d[c]，就说明[start:i]之内存在重复，直接把start移到d[c]+1
# 传统方法要维护d等于所有substring中的unique字符，其实不必
        for i,c in enumerate(s):
            if c in d and start<=d[c]:
                start = d[c]+1
            else:
                Max = max(Max, i-start+1)
            d[c] = i
        
        return Max