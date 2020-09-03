class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # 非常巧妙的方法，如果s包含n个重复的串，那么s+s包含2n个。把s+s去掉头字母和尾字母，只剩2n-2个
        # 在这2n-2个中，去寻找s是否存在。正常情况下，应该能找到s，就返回true。
        # 如果s中包含一个非重复的子串，那么2n-2中一定找不到s
        S = s+s
        S = S[1:-1]
        if S.find(s)!=-1: return True
        return False