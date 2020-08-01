class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # 从左往右遍历，如果后一个数小于前一个数，删除前一个数
        # 注意开头的0，全是同一个数字，全是0的情况
        if k==len(num): return '0'
        while k>0 and len(num)>1:
            done = True
            for i in range(1, len(num)):
                if int(num[i]) < int(num[i-1]):
                    num = num[:i-1]+num[i:]
                    k-=1
                    done = False
                    break
            if done: break
                
        while len(num)>1 and num[0]=='0': num = num[1:]
        if k==0: return num
        elif k>=len(num): return '0'
        else: return num[:-k]