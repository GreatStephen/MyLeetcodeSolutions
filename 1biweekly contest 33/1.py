class Solution(object):
    def thousandSeparator(self, n):
        ans = ''
        temp = ''
        count = 3
        s = str(n)
        for c in reversed(s):
            temp = c+temp
            count -= 1
            if not count:
                ans = '.'+temp+ans
                temp = ''
                count = 3
                # print ans
        
        if len(temp)>0:
            ans = temp+ans
            return ans
        else:
            return ans[1:]
        
