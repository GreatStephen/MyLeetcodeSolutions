class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        # calculate the money for everyone
        debt = []
        ptoi = {}
        idx = 0
        for t in transactions:
            if t[0] not in ptoi:
                ptoi[t[0]] = idx
                idx += 1
                debt.append(0)
            if t[1] not in ptoi:
                ptoi[t[1]] = idx
                idx += 1
                debt.append(0)
            debt[ptoi[t[0]]] -= t[2]
            debt[ptoi[t[1]]] += t[2]
        
        # print(debt)
        
        
        # DFS
        # 对当前第一个debt!=0的人，把他的钱全部给下一个异号的人，然后从idx+1开始继续DFS
        self.ans = float('inf')
        def DFS(idx, cur):
            while idx<len(debt) and debt[idx]==0:
                idx += 1
            if idx==len(debt):
                self.ans = min(self.ans, cur)
            for j in range(idx+1, len(debt)):
                if debt[j]*debt[idx]<0:
                    debt[j] += debt[idx]
                    DFS(idx+1, cur+1)
                    debt[j] -= debt[idx]
        
        
        DFS(0, 0)
        return self.ans
            