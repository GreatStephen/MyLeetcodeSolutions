class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        # 技巧性很高。这题允许数字重复，所以难度不高。目标是找到最左侧的不符合条件的数字，把它-1，然后后面的数字全部填9
        # 从右向左，如果碰到下降的两个数字，就把左边的数字-1，然后记录它的位置
        # 遍历完之后，我们得到了应该减1的数字。把它减1，剩下的填9
        if N<10: return N
        num = str(N)
        j = len(num)
        val = int(num[-1])
        # 之所以倒序遍历，是因为把某一个数字-1之后，它可能和它左边的数字再组成一个下降序列
        # 所以干脆倒序遍历，碰到下降序列就-1，直到不再出现下降序列
        for i in range(len(num)-1, 0, -1):
            if int(num[i-1])>val:
                j = i-1
                val = int(num[i-1])-1
            else:
                val = int(num[i-1])
        if j==len(num):
            return N
        
        
        
        ans = num[:j]
        for i in range(j, len(num)):
            if i==j:
                ans += str(int(num[i])-1) # 第一个数字-1
            else:
                ans += '9' # 剩下的填9
        
        return int(ans)