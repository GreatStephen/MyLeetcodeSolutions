class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        # 记录remain字符串，和下一个s1循环连接在一起，然后看这个字符串是否循环过，如果循环过，就把上次的结果拿出来
        d = {}
        ans = 0
        remain = ''
        for i in range(n1):
            count = 0
            lastidx = -1
            temps = remain+s1
            if temps in d: # a loop
                count = d[temps][0]
                remain = d[temps][1]
                ans += count
                continue
            
            # not loop yet, count how many s2 is in temps
            idxs2 = 0
            for j in range(len(temps)):
                if temps[j]==s2[idxs2]:
                    idxs2 += 1
                    if idxs2==len(s2):
                        lastidx = j
                        count += 1
                        idxs2 = 0
            
            remain = temps[lastidx+1:]
            d[temps] = [count, remain]
            ans += count
        
        return ans//n2