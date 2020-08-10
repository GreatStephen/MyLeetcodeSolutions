class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        # 用一个数字cur=0x00000，每位代表一个元音
        # 出现某个元音时，将其对应的位与1异或，然后查以前出没出现过这个cur
        # 如果出现过，说明这两个位置之间，所有元音的数量都是偶数，取j-i即可
        letters = {'a':0, 'e':1,'i':2, 'o':3, 'u':4}
        cur = 0
        record = {0:-1}
        ans = 0
        for i,c in enumerate(s):
            if c in letters:
                cur ^= (1<<letters[c])
            if cur in record:
                ans = max(ans, i-record[cur])
            else:
                record[cur] = i
        return ans