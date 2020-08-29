# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution(object):
    # 用两次Rand7()，产生49个数。抛弃最后9个，如果结果落在0-39之间，即可轻松产生10以内的数
    
    def rand10(self):
        # 这里模拟了7进制数字，先产生一个十位数字，*7，再产生一个个位数字。这样就把它变成
        # [0:39]的连续十进制数。
        ans = (rand7()-1)*7 + rand7()-1 
        while ans>=40: # 大于40就抛弃
            ans = (rand7()-1)*7 + rand7()-1
        return ans%10 + 1