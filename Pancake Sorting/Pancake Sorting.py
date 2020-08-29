class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        self.cur, ans = A, []
        # 找到最大值的下标idx，然后将[:idx]翻转，再翻转整个list，最大值就跑到最后一位去了
        # 然后去掉最后一位，剩下的list继续这个过程
        def helper():
            idx = self.cur.index(len(self.cur))
            if idx!=len(self.cur)-1:
                ans.append(idx+1)
                ans.append(len(self.cur))
            self.cur = self.cur[:idx:-1]+self.cur[:idx]
        
        
        while self.cur:
            helper()
        return ans