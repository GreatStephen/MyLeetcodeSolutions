class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        # 字符串拼接问题，很简单
        a = ''
        ans = ''
        S = S.split(' ')
        
        for s in S:
            temp = s
            if s[0] not in 'aeiouAEIOU':
                temp = temp[1:]+temp[0]
            a += 'a'
            temp += 'ma' + a
            ans += temp + ' '
        return ans[:-1]