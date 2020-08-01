class Solution:
    def numberOfSubstrings(self, s):
        d, ans = {'a':-1, 'b':-1, 'c':-1}, 0
        for i,v in enumerate(s):
            d[v] = i
            ans += min(d.values())+1
        return ans